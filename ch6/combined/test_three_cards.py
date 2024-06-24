import pytest
import cards


@pytest.fixture(scope="function")
def cards_db(session_cards_db, request, faker):
    db = session_cards_db
    db.delete_all()
    # support for `@pytest.mark.num_cards(<some number>)`
    # random seed
    faker.seed_instance(101)
    m = request.node.get_closest_marker("num_cards")
    if m and len(m.args) > 0:
        num_cards = m.args[0]
        for _ in range(num_cards):
            db.add_card(
            cards.Card(summary=faker.sentence(), owner=faker.first_name())
            )

    return db

@pytest.fixture(scope="function")
def cards_db_three_cards(session_cards_db):
    db = session_cards_db
    # start with empty
    db.delete_all()
    # add three cards
    db.add_card(cards.Card("Learn something new"))
    db.add_card(cards.Card("Build useful tools"))
    db.add_card(cards.Card("Teach others"))
    return db


def test_zero_card(cards_db):
    assert cards_db.count() == 0


@pytest.mark.num_cards(3)
def test_three_card(cards_db_three_cards):
    cards_db = cards_db_three_cards
    assert cards_db.count() == 3