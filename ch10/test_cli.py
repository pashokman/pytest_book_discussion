import cards
from test_typer_testing import cards_cli


def test_add_with_owner(mock_cardsdb):
    cards_cli("add some task -o brian")
    expected = cards.Card("some task", owner="brian", state="todo")
    mock_cardsdb.add_card.assert_called_with(expected)


def test_delete_invalid(mock_cardsdb):
    mock_cardsdb.delete_card.side_effect = cards.api.InvalidCardId
    out = cards_cli("delete 25")
    assert "Error: Invalid card id 25" in out