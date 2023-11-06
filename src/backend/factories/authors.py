import factory

from backend.models import AuthorModel
from backend.db import SessionManager


manager = SessionManager()
session = manager.session


class AuthorFactory(factory.alchemy.SQLAlchemyModelFactory):

    class Meta:
        model = AuthorModel
        sqlalchemy_session = session
        sqlalchemy_session_persistence = "commit"

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    books = factory.RelatedFactoryList("backend.factories.BookFactory", factory_related_name="author", size=10)
