import json
import logging
import psycopg

from bs4 import BeautifulSoup as BS
import requests
from tqdm import tqdm

from backend.src.app.settings import settings

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


def get_session():
    return psycopg.connect(
        dbname=settings.db.DB_NAME,
        user=settings.db.DB_USER,
        password=settings.db.DB_PASSWORD,
        host=settings.db.DB_HOST,
        port=settings.db.DB_PORT,
    )


def save_to_db(items: tuple):
    with get_session() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO words (word) 
                VALUES (%s)
                ON CONFLICT (word) DO UPDATE SET word = EXCLUDED.word
                RETURNING id
            """,
                (word,),
            )
            word_id = cur.fetchone()[0]

            # 2. Вставляем категории (если их еще нет)
            for category in categories:
                cur.execute(
                    """
                    INSERT INTO categories (name)
                    VALUES (%s)
                    ON CONFLICT (name) DO UPDATE SET name = EXCLUDED.name
                    RETURNING id
                """,
                    (category,),
                )
                category_id = cur.fetchone()[0]

                # 3. Связываем слово и категорию
                cur.execute(
                    """
                    INSERT INTO category_word (category_id, word_id)
                    VALUES (%s, %s)
                    ON CONFLICT DO NOTHING
                """,
                    (category_id, word_id),
                )

            conn.commit()
            return word_id


def start_process():
    url = "https://rushengl.com/vocabularytop.php"
    response = requests.get(url)
    soup = BS(response.text, "html.parser")
    raw_data = soup.find_all("script", type="application/ld+json")

    levels = None
    try:
        json_data = json.loads(raw_data[0].string)
        if json_data.get("@graph", None):
            for item in tqdm(json_data["@graph"]):
                if (
                    item.get("@type") == "ItemList"
                    and item.get("@id")
                    == "https://rushengl.com/vocabularytop.php?level=1#articleList"
                ):
                    levels = item.get("itemListElement", [])

    except json.JSONDecodeError as e:
        logger.error(f"Ошибка парсинга JSON: {e}")

    data_set = []
    for item in tqdm(levels, desc="Процесс обработки страниц с уровнями"):
        page = requests.get(item["item"])
        soup = BS(page.text, "html.parser")
        table = soup.find("table", id="mtable")
        words_data = []
        for row in table.find_all("tr", class_="linevis"):
            word = (
                row.find("td", class_="wordshow").text.strip()
                if row.find("td", class_="wordshow")
                else None
            )

            transcription = (
                row.find_all("td", class_="wordshow")[1].text.strip()
                if len(row.find_all("td", class_="wordshow")) > 1
                else None
            )

            translation = (
                row.find("td", class_="intershow").text.strip()
                if row.find("td", class_="intershow")
                else None
            )

            if word and translation:
                words_data.append(
                    {
                        "word": word,
                        "transcription": transcription,
                        "translation": translation,
                    }
                )
        data_set.append(
            {
                "category": item["name"],
                "quantity": len(words_data),
                "words": words_data,
            }
        )

    print(json.dumps(data_set, indent=4, ensure_ascii=False))


if __name__ == "__main__":
    start_process()
