from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        self.first_name: str = first_name
        self.is_alive: bool = is_alive
        self.family_name: str = "Baratheon"
        self.eyes: str = "brown"
        self.hairs: str = "dark"

    def die(self) -> None:
        """Implementation of die - Sets is_alive to false"""
        self.is_alive = False

    def __str__(self) -> str:
        """Human readable string representing the object."""
        return (
            f"Character Name: {self.first_name}, "
            f"Family Name: {self.family_name}, "
            f"Eyes Color: {self.eyes}, "
            f"Hair Color: {self.hairs}, Is Alive: {self.is_alive}"
        )

    def __repr__(self) -> str:
        """string representation of the object."""
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"


class Lannister(Character):
    """Representing the Lannister family."""

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        self.first_name: str = first_name
        self.is_alive: bool = is_alive
        self.family_name: str = "Lannister"
        self.eyes: str = "blue"
        self.hairs: str = "light"

    def die(self) -> None:
        """Implementation of die - Sets is_alive to false"""
        self.is_alive = False

    def __str__(self) -> str:
        """Human readable string representing the object."""
        return (
            f"Character Name: {self.first_name}, "
            f"Family Name: {self.family_name}, "
            f"Eyes Color: {self.eyes}, "
            f"Hair Color: {self.hairs}, Is Alive: {self.is_alive}"
        )

    def __repr__(self) -> str:
        """string representation of the object."""
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"

    @classmethod
    def create_lannister(
        cls, first_name: str, is_alive: bool = True
    ) -> Character:
        """class method that serves as factory method for Lannister class."""
        return cls(first_name, is_alive)
