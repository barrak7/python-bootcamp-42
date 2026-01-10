def get_shape(lst: list) -> str:
    """return the shape of the given list"""
    return f"({len(lst)}, {len(lst[0])})"


def slice_me(family: list, start: int, end: int) -> list:
    """
    print the shape of the list, slice it given the start and end offsets,
    print the new shape, and return the slice.

    Checks if the given list is 2D,
    if the nested lists are of the same size,
    and if the indexes are out of range.
    If anything goes wrong, a ValueError is raised.

    Parameters:
    ----------
    family (list[list]): 2D list
    start, end (int): start and end index for slice

    Returns:
    -------
    slice_ (list[list]): 2D list after slicing.
    """
    slice_: list = []

    try:
        assert isinstance(family, list), "First argument must be a 2D list"

        for i, v in enumerate(family):
            assert isinstance(v, list), "First argument must be a 2D list"
            assert len(v) == len(family[i - 1]), "Lists must be the same size"

        print(f"My shape is : {get_shape(family)}")

        slice_ = family[start:end]

        print(f"My new shape is : {get_shape(slice_)}")
    except Exception as e:
        print("Error:", e)

    return slice_
