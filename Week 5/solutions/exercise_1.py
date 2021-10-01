# Exercise 1 - Solution


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def age_difference(self, other: 'Person') -> int:
        return self.age - other.age

    def __str__(self) -> str:
        return f'Your name is {self.name} and you are {self.age} years old'


def main():
    name = str(input('Enter your name: '))
    age = int(input('Enter your age: '))
    person_1 = Person(name, age)

    ai_person = Person('Computer', 100)
    print(str(person_1))
    age_diff = ai_person.age_difference(person_1)
    print(f'{ai_person.name} is {age_diff} years older than {person_1.name}')


main()
