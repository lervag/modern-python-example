from modern_python_example.greeting import Person, greeting


def main() -> None:
    person = Person(name="World")
    print(greeting(person.name))
