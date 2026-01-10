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
