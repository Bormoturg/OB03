# Базовый класс Animal, содержащий общие атрибуты и методы
class Animal:
    def __init__(self, name, age):
        self.name = name  # Имя животного
        self.age = age    # Возраст животного

    def make_sound(self):
        raise NotImplementedError("Subclasses must implement this method")

    def eat(self):
        print(f"{self.name} is eating.")


# Подкласс Bird, наследующий от Animal
class Bird(Animal):
    def make_sound(self):
        print(f"{self.name} says tweet!")


# Подкласс Mammal, наследующий от Animal
class Mammal(Animal):
    def make_sound(self):
        print(f"{self.name} says woof!")


# Подкласс Reptile, наследующий от Animal
class Reptile(Animal):
    def make_sound(self):
        print(f"{self.name} says hiss!")


# Функция для демонстрации полиморфизма
def animal_sound(animals):
    for animal in animals:
        animal.make_sound()


# Класс Zoo, использующий композицию для хранения животных и сотрудников
class Zoo:
    def __init__(self):
        self.animals = []  # Список животных в зоопарке
        self.staff = []    # Список сотрудников зоопарка

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, staff_member):
        self.staff.append(staff_member)


# Классы для сотрудников зоопарка
class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"{self.name} is feeding {animal.name}")


class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"{self.name} is healing {animal.name}")


# Демонстрация использования классов
if __name__ == "__main__":
    # Создание объектов животных
    bird = Bird("Tweety", 2)
    mammal = Mammal("Rover", 4)
    reptile = Reptile("Sly", 5)

    # Создание объектов сотрудников
    keeper = ZooKeeper("Alice")
    vet = Veterinarian("Bob")

    # Создание зоопарка и добавление животных и сотрудников
    zoo = Zoo()
    zoo.add_animal(bird)
    zoo.add_animal(mammal)
    zoo.add_animal(reptile)
    zoo.add_staff(keeper)
    zoo.add_staff(vet)

    # Демонстрация полиморфизма
    animal_sound(zoo.animals)

    # Демонстрация работы сотрудников
    keeper.feed_animal(mammal)
    vet.heal_animal(reptile)
