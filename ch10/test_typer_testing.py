from typer.testing import CliRunner
from cards.cli import app


runner = CliRunner()


def cards_cli(command_string):
    command_list = command_string.split()
    result = runner.invoke(app, command_list)
    output = result.stdout.rstrip()
    return output


def test_typer_runner():
    result = cards_cli("version")
    print()
    print(f"version: {result}")

    result = cards_cli("list -o brian")
    print(f"list:\n{result}")