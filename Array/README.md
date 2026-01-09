# Array
An introduction into python arrays.

## Ex00: Give my BMI
Create two functions:
```py
def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
```
- Takes two lists of int or float values representing height and weight, respectively, and returns a list of int or float values representing the **BMI scale**.

and
```py
def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
```
- Takes a list of bmi scales and a limit. Returns a list of bool values indicating whether each scale is above the limit or not.
