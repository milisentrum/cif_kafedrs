class Animal:
    def __init__(self, name: str, age: int):

        self.name = name
        self.age = age

    def make_sound(self) -> str:

        return "Some generic animal sound"


class Dog(Animal):

    def __init__(self, name: str, age: int, breed: str):
        super().__init__(name, age)
        self.breed = breed

    def make_sound(self) -> str:
        return "Woof woof!"


if __name__ == "__main__":
    generic_animal = Animal("Generic", 5)

    doggo = Dog("Buddy", 3, "Golden Retriever")

    print(generic_animal.make_sound())
    print(doggo.make_sound())
