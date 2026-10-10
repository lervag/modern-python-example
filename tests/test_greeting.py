import pytest
from pydantic import ValidationError

from modern_python_example.greeting import Person, first, greeting


def test_greeting() -> None:
    assert greeting("World") == "Hello World"


def test_first() -> None:
    assert first(["a", "b"]) == "a"


def test_person_validates_name() -> None:
    with pytest.raises(ValidationError):
        Person.model_validate({"name": 42})
