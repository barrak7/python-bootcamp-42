class calculator:
    """
    Perform dot-product, addition, subtraction on 2 lists / vectors of floats.

    This class has only static methods since the operations are performed
    on external - class independent - variables.

    No error handling was required.
    """

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
        Performs dot product over V1 and V2

        It is assumed that the input is always valid.
        """
        re: float = 0

        for i in range(len(V1)):
            re += V1[i] * V2[i]

        print("Dot product is:", re)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
        Performs addition over V1 and V2

        It is assumed that the input is always valid.
        """
        re: list[float] = [0.0] * len(V1)

        for i in range(len(V1)):
            re[i] += V1[i] + V2[i]

        print("Add vector is:", re)

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
        Performs subtraction over V1 and V2

        It is assumed that the input is always valid.
        """
        re: list[float] = [0.0] * len(V1)

        for i in range(len(V1)):
            re[i] += V1[i] - V2[i]

        print("Sous vector is:", re)
