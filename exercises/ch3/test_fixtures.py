import pytest


@pytest.fixture()
def testing_dict():
    d = {
        "key1": "value1",
        "key2": "value2",
        "key3": "value3",
        "key4": "value4", 
        }
    return d


@pytest.fixture()
def testing_list():
    l = [1, 2, 3, 4, 5]
    print("\nFixture starts it's work")
    print(f'\nI use this list - {l}')
    yield l
    print("\nFixture ends it's work")


def test_dict_length(testing_dict):
    length = len(testing_dict)
    assert length == 4


def test_key_in_dict(testing_dict):
    keys = testing_dict.keys()
    assert "key2" in keys


def test_max_list_number(testing_list):
    assert max(testing_list) == 5