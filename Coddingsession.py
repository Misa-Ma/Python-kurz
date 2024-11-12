from abc import ABC, abstractmethod
class Figure(ABC):
    @abstractmethod
    def get_circ():
        pass
    @abstractmethod
    def get_area():
        pass
class Square(Figure):
    def __init__(self, a):
        self.a = a
    def get_circ(self):
        return 4 * self.a
    def get_area(self):
        return self.a ** 2
garden = Square(30)
print(garden.get_area())

from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def animal_sound():
        pass
    def sleep(self):
        print("Zzz")
class Dog(Animal):
    def animal_sound(self):
        print("Haf!")
class Cat(Animal):
    def animal_sound(self):
        print("Mňau")
Animal("Test")
dasenka = Dog("Dášenka")
dasenka.animal_sound()
dasenka.sleep()
micka = Cat("Micka")
micka.animal_sound()

from abc import ABC, abstractmethod
class Figure(ABC):
    @abstractmethod
    def get_circ():
        pass
    @abstractmethod
    def get_area():
        pass
class Circle(Figure):
    # statický atribut
    pi = 3.14
    def __init__(self, r):
        self.r = r
    def get_circ(self):
        return 2 * self.pi * self.r
    def get_area(self):
        return self.pi * self.r ** 2
pool = Circle(5)
print(pool.get_area())
golf_area = Circle(100)
print(golf_area.get_area())

class Projekt:
    datum_zahajeni = "projekty.datum_zahajeni"
    datum_ukonceni = "projekty.datum_ukonceni"