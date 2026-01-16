from typing import Any


class calculator:
    """
    Perform arithmetic operations on vector and scalar value.
    No error handling was required.
    """

    def __init__(self, vec: list[float]) -> None:
        """initialize internal vector."""
        self.vec: list[float] = vec

    def __add__(self, scalar: Any) -> None:
        """perform element wise addition with scalar"""
        for i in range(len(self.vec)):
            self.vec[i] += scalar

        print(self.vec)

    def __sub__(self, scalar: Any) -> None:
        """perform element wise subtraction with scalar"""
        for i in range(len(self.vec)):
            self.vec[i] -= scalar

        print(self.vec)

    def __mul__(self, scalar: Any) -> None:
        """perform element wise multiplication with scalar"""
        for i in range(len(self.vec)):
            self.vec[i] *= scalar

        print(self.vec)

    def __truediv__(self, scalar: Any) -> None:
        """perform element wise division with scalar"""
        if scalar == 0:
            print("Error: division by zero is not possible!")
            return

        for i in range(len(self.vec)):
            self.vec[i] /= scalar

        print(self.vec)
