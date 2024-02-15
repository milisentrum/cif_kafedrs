# class Book:
#     """ Базовый класс книги. """
#     def __init__(self, name: str, author: str):
#         self.name = name
#         self.author = author
#
#     def __str__(self):
#         return f"Книга {self.name}. Автор {self.author}"
#
#     def __repr__(self):
#         return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"
#
#
# class PaperBook:
#     def __init__(self, name: str, author: str, pages: int):
#         self.name = name
#         self.author = author
#         self.pages = pages
#
#     def __str__(self):
#         return f"Книга {self.name}. Автор {self.author}"
#
#
# class AudioBook:
#     def __init__(self, name: str, author: str, duration: float):
#         self.name = name
#         self.author = author
#         self.duration = duration
#
#     def __str__(self):
#         return f"Книга {self.name}. Автор {self.author}"

class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            raise ValueError("Количество страниц должно быть целым числом")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = value

    def __str__(self):
        return f"Бумажная книга {self.name}. Автор {self.author}. Количество страниц: {self.pages}"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, float):
            raise ValueError("Продолжительность должна быть числом с плавающей запятой")
        if value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом")
        self._duration = value

    def __str__(self):
        return f"Аудиокнига {self.name}. Автор {self.author}. Продолжительность: {self.duration} часов"
