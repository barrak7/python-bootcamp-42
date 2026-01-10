from numpy import ndarray
import matplotlib.pyplot as plt


def ft_invert(array: ndarray) -> ndarray:
    """Inverts the color of the image received."""
    try:
        array = 255 - array

        print(array)

        plt.imshow(array)
        plt.show()
    except Exception as e:
        print("Error:", e)

    return array


def ft_red(array: ndarray) -> ndarray:
    """Applies a red filter to the image received."""
    try:
        array = array.copy()
        array[:, :, 1:] = 0

        print(array)

        plt.imshow(array)
        plt.show()
    except Exception as e:
        print("Error:", e)

    return array


def ft_green(array: ndarray) -> ndarray:
    """Applies a green filter to the image received."""
    try:
        array = array.copy()
        array[:, :, 0] = 0
        array[:, :, 2] = 0

        print(array)

        plt.imshow(array)
        plt.show()
    except Exception as e:
        print("Error:", e)

    return array
