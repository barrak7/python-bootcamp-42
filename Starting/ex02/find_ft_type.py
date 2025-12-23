def all_thing_is_obj(object: any) -> int:
    _type: type = type(object)
    _type_name: str = _type.__name__.title()
    _types: set[str] = {"List", "Tuple", "Dict", "Set", "Str"}

    if _type_name in _types:
        if _type_name == "Str":
            _type_name = f"{object} is in the kitchen"
        print(f"{_type_name} : {_type}")
    else:
        print("Type not found")

    return 42
