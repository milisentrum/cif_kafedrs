from typing import Union


class AbstractObject:
    def __init__(self, name: str, description: str):

        self.name = name
        self.description = description

    def get_info(self) -> str:
        ...

    def interact(self, other: 'AbstractObject') -> str:
        ...


class PhysicalObject(AbstractObject):
    def __init__(self, name: str, description: str, weight: float, material: str):

        super().__init__(name, description)
        self.weight = weight
        self.material = material

    def move(self, destination: str) -> str:

        ...

    def break_down(self) -> str:

        ...


class DigitalObject(AbstractObject):

    def __init__(self, name: str, description: str, size_in_gb: float, format: str):

        super().__init__(name, description)
        self.size_in_gb = size_in_gb
        self.format = format

    def compress(self) -> str:

        ...

    def encrypt(self) -> str:

        ...


if __name__ == "__main__":
    import doctest

    doctest.testmod()
