from click.testing import CliRunner

from uwuify import cli

# TODO: expand tests


def test_main_basic():
    runner = CliRunner()

    # tests piping
    result = runner.invoke(cli.main, input="hello")
    assert result.exit_code == 0
    assert result.output == "hewwo\n"

    result = runner.invoke(cli.main, ["hello"])
    assert result.exit_code == 0
    assert result.output == "hewwo\n"


def test_main_flags():
    runner = CliRunner()

    result = runner.invoke(cli.main, "--nouwu hello".split(" "))
    assert result.exit_code == 0
    assert result.output == "hello\n"

    result = runner.invoke(cli.main, "--yu --nouwu you".split(" "))
    assert result.exit_code == 0
    assert result.output == "yoyu\n"

    result = runner.invoke(cli.main, "--stutter hello".split(" "))
    assert result.exit_code == 0
    assert result.output == "h-hewwo\n"
