# OOP
learn oop in python: abstract class, inheritance, overriding, property, and operator overriding.

## Ex00: GOT S1E9
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

## Ex01: GOT S1E7
Implement a class which inherits from `Character` but doesn't use its constructor. It should have a factory method to create an object of its type. It should also implement `__repr__` and `__str__` methods.

A factory method is  a **class method** which creates an object of its class. A class method is a method that belongs to the class and is accessible without the need for an instance of the class.  
Its first argument is the class itself.

`__repr__` and `__str__` are dunder methods. Dunder methods in python are methods with double underscores `__` before and after their names. They allow you to define how python built in operations deal with your custom class.  
For example, `__str__` allows you to set a custom behaviour for when print is called on an object of your class, or when it is converted to a string.

```py
# factory method
class Lannister(Character):
    """Representing the Lannister family."""

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        self.first_name: str = first_name
        self.is_alive: bool = is_alive
        self.family_name: str = "Lannister"
        self.eyes: str = "blue"
        self.hairs: str = "light"

    def die(self) -> None:
        """Implementation of die - Sets is_alive to false"""
        self.is_alive = False

    # dunder method
    def __str__(self) -> str:
        """Human readable string representing the object."""
        return (
            f"Character Name: {self.first_name}, "
            f"Family Name: {self.family_name}, "
            f"Eyes Color: {self.eyes}, "
            f"Hair Color: {self.hairs}, Is Alive: {self.is_alive}"
        )
    
    # dunder method
    def __repr__(self) -> str:
        """string representation of the object."""
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"

    # Factory method
    @classmethod
    def create_lannister(
            cls, first_name: str, is_alive: bool = True
            ) -> Character:
        """class method that serves as factory method for Lannister class."""
        return cls(first_name, is_alive)
```

## Ex02: Now it's weird!
This exercise introduces the diamond problem of inheritance. It also introduces python's built-in `property`

Create a class that inherits from 2 Other classes that subclass the same class. This will create the diamond problem, but python deals with this problem natively using [The Python Method Resolution Order - MRO](https://docs.python.org/3/howto/mro.html#python-2-3-mro)

The class should have setter and getters for some of its attributes, and it should use the `property` class.  
The property class / decorator allows you to customise access to the attribute using `setter` and `getter` methods.

```py
# diamond trap - python automatically resolves the problem by giving precedence to the first class
class King(Baratheon, Lannister):
    """False king."""

    def get_eyes(self) -> str:
        """eyes getter"""
        return self._eyes

    def set_eyes(self, color: str) -> None:
        """eyes setter"""
        self._eyes = color

    # eyes property - access and assignment to `eyes` will be through `get_eyes` and `set_eyes` methods
    eyes = property(get_eyes, set_eyes)
```

## Ex03: Calculate my vector
in this exercise, create a class `calculator` that performs arithmetic operations on a vector with a scalar.  
This was done through operator overloading. i.e. redefining / defining the behaviour of the `+-*/` operators for your class.

This can be done by implementing the dunder methods: `__add__`, `__sub__`, `__mul__`, and `__truediv__`
