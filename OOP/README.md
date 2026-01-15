# OOP
learn oop in python: abstract class, inheritance, overriding, property, and operator overriding.

# Ex00: GOT S1E9
Implement an abstract class with an abstract method, and then inherit from it and implement the abstract method.

Features of an Abstract Class:
- You can't instantiate from it.
- It has abstract methods that can function as an interface for child classes.

```py
# Abstract class
class Character(ABC):
    """abstract class with abstract method"""
    def __init__(self, first_name: str, is_alive=True) -> None:
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self) -> None:
        """Abstract method - Sets is_alive to false"""

# inheritance from and implementation of abstract class
class Stark(Character):
    """Child class of Character"""

    def die(self) -> None:
        """Implementation of die - Sets is_alive to false"""
        self.is_alive = False
```
