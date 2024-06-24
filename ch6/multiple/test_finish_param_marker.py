from pathlib import Path
from tempfile import TemporaryDirectory
import pytest
import cards


@pytest.fixture(scope='session')
def db():
    """CardsDB object connected to a temporary database"""
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir)
        db = cards.CardsDB(db_path)
        yield db
        db.close()


@pytest.fixture(scope="function")
def cards_db(db):
    """CardsDB object that's empty"""
    db.delete_all()
    return db


@pytest.mark.parametrize(
    "start_state",
    [
        "todo",
        pytest.param("in prog", marks=pytest.mark.smoke),
        "done",
    ],
    )
def test_finish_func(cards_db, start_state):
    i = cards_db.add_card(cards.Card("foo", state=start_state))
    cards_db.finish(i)
    c = cards_db.get_card(i)
    assert c.state == "done"
