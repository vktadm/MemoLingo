from backend.src.app.services import CryptoService


def test_hash_password__success(
    crypto_service: CryptoService,
):
    password = "password"
    hashed_password = crypto_service.hash_password(password)

    assert crypto_service.validate_password(
        password=password,
        hashed_password=hashed_password,
    )


def test_hash_password__fail(
    crypto_service: CryptoService,
):
    password = "password"
    hashed_password = crypto_service.hash_password(password)

    incorrect_password = "incorrect_password"
    hashed_incorrect_password = crypto_service.hash_password(incorrect_password)

    assert not crypto_service.validate_password(
        password=incorrect_password,
        hashed_password=hashed_password,
    )
    assert hashed_incorrect_password != hashed_password
