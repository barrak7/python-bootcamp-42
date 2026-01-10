from PIL import Image
import numpy as np
from numpy import ndarray


def ft_load(path: str) -> ndarray:
    """
    load image file located in path, print its shape,
    and return its RGB values as a numpy array.

    Note: the image path should be either a full path,
        or a path relative to the executing script.
    """
    img_arr: ndarray

    try:
        with Image.open(path) as img:
            img_arr = np.array(img)

    except Exception as e:
        print("Error:", e)

        return -1

    return img_arr
