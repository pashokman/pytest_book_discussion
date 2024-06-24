from unittest import mock
from my_info import home_dir
from pathlib import Path


def test_path():
    with mock.patch.object(home_dir, autospec=True):
        path = Path("/users/fake_user")
        assert home_dir() == "C:\\Users\\PaulKP"

