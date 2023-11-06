import factory
from random import randint

from backend.models import UserModel


from backend.db import SessionManager
from backend.services import UserService
from backend.factories import BookFactory


manager = SessionManager()
session = manager.session


class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = UserModel
        sqlalchemy_session = session
        sqlalchemy_session_persistence = "commit"

    username = factory.Faker("user_name")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    hashed_password = factory.LazyFunction(lambda: UserService.get_password_hash("Elektryk1@"))

    @factory.post_generation
    def add_saved_books(self, create, extracted, **kwargs):
        if not create:
            return

        for _ in range(randint(0, 2)):
            self.saved_books.append(BookFactory.create())