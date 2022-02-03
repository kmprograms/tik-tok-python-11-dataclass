from dataclasses import dataclass, asdict, field

"""
    Na początek utworzymy prostą klasę Person.
"""
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'<Person [{self.name} {self.age}]>'

    def __str__(self):
        return f'Person [{self.name} {self.age}]'


    """
        Kiedy chcesz porównywać obiekty klasy Person
        musisz dodatkowo zaimplementować metody
        __eq__, __hash__, itd.
    """

p = Person('ADAM', 20)
print(p)
print(repr(p))

"""
    Zapis takiej klasy można znacznie uprościć dzięki
    dekoratorowi @dataclass.
    Pokażę to na przykładzie klasy Student.
    Dekorator zajmie się automatycznym wygenerowaniem
    metod takich jak __init__, __repr__, __str__,
    __eq__, __hash__ i innych
"""

@dataclass
class Student:
    name: str
    age: int

s = Student('ADAM', 20)
print(s)
print(repr(s))

"""
    Możesz stosować wartości domyślne dla pól klasy
"""
@dataclass
class Worker:
    name: str = 'ADAM'
    age: int = 18

w1 = Worker('EWA', 30)
print(w1)

w2 = Worker()
print(w2)

"""
    Atrybut frozen ustawiony na True powoduje
    wygenerowanie pól składowych read only
"""
@dataclass(frozen=True)
class Product:
    name: str
    quantity: int

pr = Product('A', 100)
print(pr)
print(pr.name)
print(pr.quantity)
# pr.name = 'AA'

"""
    Możesz ustalać właściwości autogenerowania
    dla poszczególnych pól za pomocą funkcji 
    field
"""
@dataclass
class Team:
    name: str
    points: int = field(repr=False)

t = Team('T1', 100)
# Nie uwzględniono points w __repr__ oraz __str__
print(t)
print(repr(t))
print(t.points)