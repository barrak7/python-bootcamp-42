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
