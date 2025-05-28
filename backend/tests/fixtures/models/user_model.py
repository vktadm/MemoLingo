import factory.fuzzy
from pytest_factoryboy import register
from faker import Factory

from backend.app.database import User

faker = Factory.create()


@register(_name="user")
class UserFactory(factory.Factory):
    class Meta:
        model = User

    id = factory.LazyFunction(lambda: faker.random_int())
    username = factory.LazyFunction(lambda: faker.name())
    email = factory.LazyFunction(lambda: faker.email())
    name = factory.LazyFunction(lambda: faker.sha256())
    google_access_token = factory.fuzzy.FuzzyText(length=20)
    is_active = factory.LazyFunction(lambda: faker.boolean())
