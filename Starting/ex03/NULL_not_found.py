from typing import Any


def NULL_not_found(object: Any) -> int:
    if not object or object != object:
        val: str = str(object)
        types: dict[str, str] = {
            "": "Empty:",
            "None": "Nothing: None",
            "nan": "Cheese: nan",
            "0": "Zero: 0",
            "False": "Fake: False",
        }

        if val in types:
            print(types[val], type(object))
            return 0

    print("Type not Found")
    return 1
