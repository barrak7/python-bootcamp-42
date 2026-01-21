from typing import Any


def callLimit(limit: int):
    """wrapper for callLimiter."""

    count: int = 0

    def callLimiter(function):
        """wrapper for limit_function"""

        def limit_function(*args: Any, **kwds: Any):
            """
            limits the number of executions of nonlocal `function`
            to nonlocal `limit`.

            it keeps track of the number of executions using non-
            local `count`

            Parameters:
            -----------
            *args (any): variables number of arguments
            **kwds (any): variable number of key-wor arguments.

            Returns:
            --------
            output of function(*args, **kwargs)
            """

            nonlocal count
            result: Any

            if count >= limit:
                print("Error:", function, "call too many times")
                return

            count += 1

            result = function(*args, **kwds)

            return result

        return limit_function

    return callLimiter
