from typing import Tuple


class Rover:

    def position(self) -> Tuple[int, int]:
        return (0, 0)


class TestRover:

    def test_starts_at_position_zero(self) -> None:
        rover = Rover()
        assert rover.position() == (0, 0)
