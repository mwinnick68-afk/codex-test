import pytest

from codex_test.main import _normalize_name, greet, main


@pytest.mark.parametrize(
    ("raw_name", "expected_name"),
    [
        ("Matan", "Matan"),
        ("  Matan  ", "Matan"),
        ("Ａlice", "Alice"),
    ],
)
def test_normalize_name_accepts_valid_values(raw_name: str, expected_name: str) -> None:
    assert _normalize_name(raw_name) == expected_name


def test_normalize_name_allows_boundary_length() -> None:
    assert _normalize_name("A" * 128) == "A" * 128


@pytest.mark.parametrize("raw_name", ["", " ", "\n\t"])
def test_normalize_name_rejects_empty_values(raw_name: str) -> None:
    with pytest.raises(ValueError, match="must not be empty"):
        _normalize_name(raw_name)


def test_normalize_name_rejects_control_characters() -> None:
    with pytest.raises(ValueError, match="control characters"):
        _normalize_name("Mat\x00an")


def test_normalize_name_rejects_overly_long_values() -> None:
    with pytest.raises(ValueError, match="characters or fewer"):
        _normalize_name("A" * 129)


def test_normalize_name_rejects_non_string_values() -> None:
    with pytest.raises(TypeError, match="must be a string"):
        _normalize_name(123)  # type: ignore[arg-type]


def test_greet_uses_normalized_name() -> None:
    assert greet("  Ａlice  ") == "Hello, Alice!"


def test_main_defaults_to_world(capsys: pytest.CaptureFixture[str]) -> None:
    assert main([]) == 0
    captured = capsys.readouterr()
    assert captured.out == "Hello, world!\n"
    assert captured.err == ""


def test_main_prints_greeting_for_valid_name(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["Matan"]) == 0
    captured = capsys.readouterr()
    assert captured.out == "Hello, Matan!\n"
    assert captured.err == ""


def test_main_returns_error_code_for_invalid_name(
    capsys: pytest.CaptureFixture[str],
) -> None:
    assert main(["Mat\x00an"]) == 2
    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err == "Error: name contains unsupported control characters\n"


def test_main_raises_on_argument_parse_errors(capsys: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit) as error:
        main(["Alice", "Bob"])

    captured = capsys.readouterr()
    assert error.value.code == 2
    assert "usage:" in captured.err
    assert "unrecognized arguments: Bob" in captured.err
