from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """False king."""

    def get_eyes(self) -> str:
        """eyes getter"""
        return self._eyes

    def set_eyes(self, color: str) -> None:
        """eyes setter"""
        self._eyes = color

    def get_hairs(self) -> str:
        """hairs getter"""
        return self._hairs

    def set_hairs(self, color: str) -> None:
        """hairs setter"""
        self._hairs = color

    eyes = property(get_eyes, set_eyes)
    hairs = property(get_hairs, set_hairs)
