from abc import ABC, abstractmethod


class Character(ABC):
    """abstract class with abstract method"""

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """Sets first name and optional is_alive boolean"""
        self.first_name: str = first_name
        self.is_alive: bool = is_alive

    @abstractmethod
    def die(self) -> None:
        """Abstract method - Sets is_alive to false"""


class Stark(Character):
    """Child class of abstract class Character"""

    def die(self) -> None:
        """Implementation of die - Sets is_alive to false"""
        self.is_alive = False
