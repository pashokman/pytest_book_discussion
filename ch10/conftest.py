import pytest
from unittest import mock
import cards


@pytest.fixture()
def mock_cardsdb():
    # autospec=True attribute is required because it safe us from mistakes (misspelling a method, adding or removing parameter...)
    with mock.patch.object(cards, "CardsDB", autospec=True) as CardsDS:
        yield CardsDS.return_value



@pytest.fixture(scope="session")
def tmp_db_path(tmp_path_factory):
    """Path to temporary database"""
    return tmp_path_factory.mktemp("cards_db")


@pytest.fixture(scope="session")
def session_cards_db(tmp_db_path):
    """CardsDB"""
    db_ = cards.CardsDB(tmp_db_path)
    yield db_
    db_.close()


@pytest.fixture(scope="function")
def cards_db(session_cards_db):
    """Empty CardsDB"""
    db = session_cards_db
    db.delete_all()
    return db