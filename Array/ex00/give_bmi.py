def give_bmi(
    height: list[int | float], weight: list[int | float]
) -> list[int | float]:
    """
    calculate bmi scale given list of heights and list of corresponding weights

    The lists must be of the same length, and only contain ints and floats.

    The bmi scale is calculated using the formula:
    BMI = weight / height^2

    If anything goes wrong, a ValueError exception is raised
    with a proper error message.

    Parameters:
    -----------
    height (list[int | float]): list of heights in meters.
    weight (list[int | float]): list of weights in kg.

    Returns:
    --------
    bmi_scale (list[int | float]): list of bmi scales corresponding to
        the given height and weight lists.
    """
    bmi_scale: list

    try:
        assert len(height) == len(weight), ""

        bmi_scale = [weight[i] / (height[i] ** 2) for i in range(len(height))]

    except Exception:
        raise ValueError(
            "Invalid input. Please provide 2 lists of the same length"
            " containing heights in meter and weights in kg respectively."
        )

    return bmi_scale


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Check if the bmi scale is above the limit.

    if anything goes wrong, a ValueError exception is raised
    with a usage message.

    Parameters:
    -----------
    bmi (list[int | float]): a list of bmi scales.
    limit (int): the limit.

    Returns:
    --------
    above_limit (list[bool]): list of booleans,
        true if corresponding bmi scale is higher than limit,
        false otherwise.
    """
    above_limit: list[bool]

    try:
        above_limit = [e > limit for e in bmi]
    except Exception:
        raise ValueError(
            "Invalid input. Please provide a list of bmi scale values"
            " and a numerical limit to test against."
        )

    return above_limit
