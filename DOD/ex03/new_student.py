import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """generate a 15 character long id from lower case ascii characters"""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """
    dataclass student class. Has a name, surname, active status,
    and auto-generated login and id
    """

    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(default_factory=generate_id, init=False)

    def __post_init__(self):
        """
        generate a login by combining first character of name and surname
        """
        self.login = self.name[0] + self.surname
