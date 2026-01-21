# DOD

The subject for this module states:
> "A common complaint to data scientists is that they write shitcode (by the way, only for
educational purposes you may find a lot of examples of Python shitcode [here](https://shitcode.net/latest/language/python), provided
strictly for educational purposes). Why? Because the average data scientist uses a lot of
inefficient techniques and hard coded variables and neglects object-oriented programming.
Do not be like them."

I believe this is not a truly `Data Oriented Design - DOD` module since you can't really manage memory in python, but rather it is about certain best practices of writing `clean code`

## Ex00: Calculate my statistics
calculate certain statistical values like the mean, median, 1st and 3rd quartiles, variance, and standard deviation.

This exercise introduces `*args` and `**kwargs` syntax. `args` is a list, and `kwargs` is a dictionary.
```py
def fun(*args, **kwargs):
    # code
```
The function fun, can take a variable number of positional arguments `args` and a variable number of keyword arguments `kwargs`.

I also used `function wrappers` or `decorators` to solve this exercise. A decorator in python wrappes a function call, and can modify its input and outputs.
```py
def wrapper(func):
    def inner(*args, **kwargs):
        # modify input / log
        output = func(*args, **kwargs)
        # modify output / log
        # return modified / processed output
    return inner
```
A decorator can also be quite useful for logging purposes.

## Ex01: Outer - Inner
create a function that squares x, a function that raises x to itself, and an `outer` function that takes x and a function as input, and returns an `inner` function.  
Every time this inner function is executed, it updates x with the result of function(x).

```py
def outer(x, fun):
    def inner():
        nonlocal x

        x = fun(x)

        return x

    return inner
```
The `nonlocal` keyword allows us to access and update the value x so that every time inner is executed, fun(x) is accumulated.

To get an intuition behind how `nonlocal` works, checkout [python cell objects](https://docs.python.org/3/c-api/cell.html) and [python \__closure__](https://docs.python.org/3/reference/datamodel.html#special-read-only-attributes)

## Ex02: my first decorating
In this exercise, implement a decorator which consists of 3 nested functions, `callLimit`, `callLimiter`, and `limit_function`.  
The first one, takes in a number which represents the limit. The second one takes a function for which to enforce the limit. The third one is the counter that updates the count and checks if the limit has been reached yet.

This is quite a salad, but it works.

```py
def callLimit(limit: int):
    # takes in limit, returns call limiter
    count = 0
    def callLimiter(function):
        # takes in function, returns limit function
        def limit_function(*args, **kwrags):
            # updates counter, applies limit, executes function
            nonlocal count
            
            if count >= limit:
                print("Error: execution limit exceeded")
                return
            
            result = function(*args, **kwargs)

            count += 1

            return result
        
        return limit_function
    
    return callLimiter
```
This can be used as follows:
```py
from callLimit import callLimit


@callLimit(2)
def f():
    print("f()")

# since the limit was set to 2, it will print an error on the third execution
for i in range(3):
    f()
```

## Ex03: Data Class
This exercise introduces the `dataclass` decorator. It's a quite useful tool that can automate and minimize the code needed to implement and instantiate a class.

In the example below, the decorator generates a \__init__ method, sets default factory for id, triggers a post init method for extra processing of \__init__ input, creates a \__repr__ method, and other cool stuff. [Learn More](https://docs.python.org/3/library/dataclasses.html).
```py
import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """generate a 15 character long id from lower case ascii characters"""
    return "".join(random.choices(string.ascii_lowercase, k = 15))


@dataclass
class Student:
    """
    dataclass student class. Has a name, surname, active status,
    and auto-generated login and id
    """
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(default_factory=generate_id, init=False)


    def __post_init__(self):
        """
        generate a login by combining first character of name and surname
        """
        self.login = self.name[0] + self.surname
```
