import factory

from backend.models import BookModel
from backend.db import SessionManager


manager = SessionManager()
session = manager.session


class BookFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = BookModel
        sqlalchemy_session = session
        sqlalchemy_session_persistence = "commit"

    title = factory.Faker("word")
    description = factory.Faker("text")
    author = factory.SubFactory("backend.factories.AuthorFactory")
