# TODO Написать 3 класса с документацией и аннотацией типов

from abc import ABC, abstractmethod

class AbstractTree(ABC):
    """
    Абстрактный класс, описывающий дерево.
    Атрибуты:
        species (str): Вид дерева.
        age (int): Возраст дерева (в годах).
        height (float): Высота дерева (в метрах).
    """

    def __init__(self, species: str, age: int, height: float):
        if age < 0:
            raise ValueError("Возраст дерева не может быть отрицательным.")
        if height <= 0:
            raise ValueError("Высота дерева должна быть положительной.")
        self.species = species
        self.age = age
        self.height = height


    def grow(self, years: int) -> None:
        """
        Увеличивает возраст дерева и его высоту.

        Args:
            years (int): Количество лет, на которое увеличивается возраст дерева.
                Должно быть больше 0.

        Raises:
            ValueError: Если years <= 0.

        >>> tree = AbstractTree("Oak", 10, 5.5)
        Traceback (most recent call last):
        ...
        TypeError: Can't instantiate abstract class AbstractTree with abstract methods grow
        """
        pass

    def produce_oxygen(self) -> float:
        """
        Вычисляет количество кислорода, производимого деревом в год.

        Returns:
            float: Количество кислорода в килограммах.

        >>> tree = AbstractTree("Pine", 15, 10.2)
        Traceback (most recent call last):
        ...
        TypeError: Can't instantiate abstract class AbstractTree with abstract methods grow
        """
        pass

class AbstractChair(ABC):
    """
    Абстрактный класс, описывающий стул.
    Атрибуты:
        material (str): Материал, из которого сделан стул.
        legs (int): Количество ножек.
        color (str): Цвет стула.
    """

    def __init__(self, material: str, legs: int, color: str):
        if legs <= 0:
            raise ValueError("Количество ножек должно быть положительным.")
        self.material = material
        self.legs = legs
        self.color = color


    def sit_on(self) -> bool:
        """
        Проверяет, можно ли сесть на стул.

        Returns:
            bool: True, если можно сесть на стул, иначе False.

        >>> chair = AbstractChair("wood", 4, "brown")  # doctest: +ELLIPSIS
        Traceback (most recent call last):
        ...
        TypeError: Can't instantiate abstract class AbstractChair with abstract methods sit_on
        """
        pass


    def repair(self) -> None:
        """
        Ремонтирует стул, если он сломан.

        >>> chair = AbstractChair("metal", 4, "black")  # doctest: +ELLIPSIS
        Traceback (most recent call last):
        ...
        TypeError: Can't instantiate abstract class AbstractChair with abstract methods sit_on
        """
        pass

class AbstractFacebookPost(ABC):
    """
    Абстрактный класс, описывающий пост в Facebook.
    Атрибуты:
        content (str): Содержимое поста.
        author (str): Автор поста.
        likes (int): Количество лайков на посте.
    """

    def __init__(self, content: str, author: str, likes: int):
        if likes < 0:
            raise ValueError("Количество лайков не может быть отрицательным.")
        self.content = content
        self.author = author
        self.likes = likes


    def like(self) -> None:
        """
        Увеличивает количество лайков на 1.

        >>> post = AbstractFacebookPost("Hello, world!", "John", 10)  # doctest: +ELLIPSIS
        Traceback (most recent call last):
        ...
        TypeError: Can't instantiate abstract class AbstractFacebookPost with abstract methods like
        """
        pass


    def share(self) -> None:
        """
        Делится постом с другими пользователями.

        >>> post = AbstractFacebookPost("Check this out!", "Alice", 5)  # doctest: +ELLIPSIS
        Traceback (most recent call last):
        ...
        TypeError: Can't instantiate abstract class AbstractFacebookPost with abstract methods like
        """
        pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()
