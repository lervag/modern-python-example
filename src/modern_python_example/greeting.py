from pydantic import BaseModel


class Person(BaseModel):
    name: str


def greeting(name: str) -> str:
    return "Hello " + name


def first[T](items: list[T]) -> T:
    return items[0]
