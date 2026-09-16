class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


def create_person_list(people: list) -> list:
    arr = []
    for item in people:
        Person.people[item["name"]] = Person(item["name"], item["age"])

    for item in people:
        new_person = Person(item["name"], item["age"])

        new_person = Person.people[item["name"]]

        if item.get("wife") and item["wife"] is not None:
            new_person.wife = Person.people[item["wife"]]

        if item.get("husband") and item["husband"] is not None:
            new_person.husband = Person.people[item["husband"]]

        arr.append(new_person)
    return arr
