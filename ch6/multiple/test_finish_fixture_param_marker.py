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


@pytest.fixture(
    params=[
        "todo",
        pytest.param("in prog", marks=pytest.mark.smoke),
        "done",
    ]
)
def start_state_fixture(request):
    return request.param

def test_finish_fix(cards_db, start_state_fixture):
    i = cards_db.add_card(cards.Card("foo", state=start_state_fixture))
    cards_db.finish(i)
    c = cards_db.get_card(i)
    assert c.state == "done"