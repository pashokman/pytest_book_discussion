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


@pytest.mark.smoke
def test_start(cards_db):
    """
    start changes state from "todo" to "in prog"
    """
    i = cards_db.add_card(cards.Card("foo", state="todo"))
    cards_db.start(i)
    c = cards_db.get_card(i)
    assert c.state == "in prog"


@pytest.mark.exception
def test_start_non_existent(cards_db):
    """
    Shouldn't be able to start a non-existent card.
    """
    any_number = 123 # any number will be invalid, db is empty
    with pytest.raises(cards.InvalidCardId):
        cards_db.start(any_number)
