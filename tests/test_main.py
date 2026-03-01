from codex_test.main import greet


def test_greet() -> None:
    assert greet("Matan") == "Hello, Matan!"

