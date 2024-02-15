# if __name__ == "__main__":
#     # Write your solution here
#     pass


class Animal:
    """Базовый класс животного."""

    def __init__(self, name: str, age: int):
        """
        Конструктор класса Animal.

        Args:
            name (str): Имя животного.
            age (int): Возраст животного.
        """
        self.name = name
        self.age = age

    def make_sound(self) -> str:
        """
        Метод для издания звука.

        Returns:
            str: Звук, издаваемый животным.
        """
        return "Some generic animal sound"


class Dog(Animal):
    """Класс собаки, наследуется от класса Animal."""

    def __init__(self, name: str, age: int, breed: str):
        """
        Конструктор класса Dog.

        Args:
            name (str): Имя собаки.
            age (int): Возраст собаки.
            breed (str): Порода собаки.
        """
        super().__init__(name, age)
        self.breed = breed

    def make_sound(self) -> str:
        """
        Перегрузка метода издания звука для собаки.

        Returns:
            str: Лай собаки.
        """
        return "Woof woof!"


if __name__ == "__main__":
    # Создание объекта базового класса Animal
    generic_animal = Animal("Generic", 5)

    # Создание объекта дочернего класса Dog
    doggo = Dog("Buddy", 3, "Golden Retriever")

    # Пример использования метода make_sound() для каждого объекта
    print(generic_animal.make_sound())  # Вывод: Some generic animal sound
    print(doggo.make_sound())           # Вывод: Woof woof!
