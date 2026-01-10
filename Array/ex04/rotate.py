from load_image import ft_load
from numpy import ndarray
import numpy as np
import matplotlib.pyplot as plt


def zoom() -> ndarray | None:
    """
    Loads animal.jpeg using ft_load, resizes it, and prints its array.

    if anything goes wrong when loading the image, the function returns
    silently.

    Note: "animal.jpeg" should be located in the same directory where
    the script is executed.
    """
    img: ndarray

    img = ft_load("animal.jpeg")

    if isinstance(img, int):
        return None

    img = img[130:530:, 460:860, 0]

    print("The shape of image is:", img.shape)

    print(img)

    return img


def rotate() -> None:
    """
    transpose the "animal.jpeg" image, i.e. rotate it, and display it.

    The color values are mapped to gray using `cmap` because the image
    is 2D.

    if anything goes wrong when loading the image, the function returns
    silently.

    Note: "animal.jpeg" should be located in the same directory where
    the script is executed.
    """
    img: ndarray = zoom()

    if img is None:
        return

    img = np.hsplit(img, 400)
    img = np.stack(img).reshape(400, 400)

    print("New shape after Transpose:", img.shape)
    print(img)

    plt.imshow(img, cmap="gray")
    plt.show()


def main() -> None:
    """calls rotate()"""
    try:
        rotate()
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
