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


def ft_blue(array: ndarray) -> ndarray:
    """Applies a blue filter to the image received."""
    try:
        array = array.copy()
        array[:, :, :2] = 0

        print(array)

        plt.imshow(array)
        plt.show()
    except Exception as e:
        print("Error:", e)

    return array


def ft_grey(array: ndarray) -> ndarray:
    """Applies a grey filter to the image received."""
    try:
        array = array.copy()
        m = array.mean(2)

        array[:, :, 0] = m
        array[:, :, 1] = m
        array[:, :, 2] = m

        print(array)

        plt.imshow(array)
        plt.show()
    except Exception as e:
        print("Error:", e)

    return array
