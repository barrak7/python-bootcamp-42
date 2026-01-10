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

## Ex01: 2D Array
Working with 2D arrays using lists.

It introduces the concept of slicing. Slicing is a syntax that allows you to take elements from an array given a starting and end position. A step offset can also be used.

The syntax is as follows:
```py
slice_ = lst[start:step:stop]
```
example:
```py
numbers = [59, 97, 0, 42, 58, 39, 6, 67, 17, 33]
print(numbers[1:4])
# -> [97, 0, 42]
```
Slicing works for reading and assigning values to a list.

Exercise Statement:
```
Write a function that takes as parameters a 2D array, prints its shape, and returns a
truncated version of the array based on the provided start and end arguments using slicing.

```
```py
# Prototype
def slice_me(family: list, start: int, end: int) -> list:

# Test
from array2D import slice_me

family = [[1.80, 78.4],
        [2.15, 102.7],
        [2.10, 98.5],
        [1.88, 75.2]]

print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))
```
```shell
# Expected output:
My shape is : (4, 2)
My new shape is : (2, 2)
[[1.8, 78.4], [2.15, 102.7]]
My shape is : (4, 2)
My new shape is : (1, 2)
[[2.15, 102.7]]
```

## Ex02: load my image
Load an image file using any library, print its shape, and return its RGB values.

For this exercises, I used the `pillow` library to load the images, then `numpy` to convert it to an array.
```py
# Prototype
def ft_load(path: str) -> ndarray:

# test
from load_image import ft_load

print(ft_load("landscape.jpg"))

# output
The shape of image is: (257, 450, 3)
[[[19 42 83]
[23 42 84]
[28 43 84]
...
[ 0 0 0]
[ 1 1 1]
[ 1 1 1]]]
```

## Ex03: Zoom on me
Load an image using the previously created function, and zoom on it by splitting its array using slicing.

After this transformation, the image is displayed using matplotlib.

## Ex04: Rotate me
Load the image, zoom on it, rotate it by transposing the array, and then display it.

The array has to be transposed manually without using numpy built-in transpose method.  
This was done by splitting the array horizontally using `np.hsplit` and then stacking the resulting arrays using `np.stack`.
```py
    img = np.hsplit(img, 400)
    img = np.stack(img)
```

## Ex05: pimp my image
create 5 functions that apply color filters to images.  
For each filter there is a restriction of the possible arithmetic operations.

The original image for reference:
[Original image](./landscape.jpg)

`ft_invert` invert the colors of the image. All arithmetic operators are allowed.
```py
img = 255 - img
```
[Inverted image](./inverted.png)

`ft_red` apply a red filter on the image using multiplication only.
```py
img[:,:,1:] *= 0
```
[Red filter](./red.png)
