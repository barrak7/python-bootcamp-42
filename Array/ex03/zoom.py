from load_image import ft_load
from numpy import ndarray
import matplotlib.pyplot as plt


def zoom() -> None:
    """
    Loads animal.jpeg using ft_load, resizes it, and displays it using
    matplotlib.

    if anything goes wrong when loading the image, the function returns
    silently.

    The color values are mapped to gray using `cmap` because the image
    is 2D.

    Note: "animal.jpeg" should be located in the same directory where
    the script is executed.
    """
    img: ndarray

    img = ft_load("animal.jpeg")

    if isinstance(img, int):
        return

    print(img)

    img = img[130:530:, 460:860, 0]

    print("New shape after slicing:", img.shape)

    print(img)

    plt.imshow(img, cmap="gray")
    plt.show()


def main() -> None:
    """calls zoom()"""
    try:
        zoom()
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
