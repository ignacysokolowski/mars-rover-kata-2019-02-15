import pytest

from mars_rover import Coordinates
from mars_rover import Direction
from mars_rover import Rover


class TestRover:

    def test_starts_at_the_given_position_and_facing_direction(self) -> None:
        rover = Rover(Coordinates(1, 3), Direction.north())
        assert rover.position() == Coordinates(1, 3)
        assert rover.direction() == Direction.north()

    @pytest.mark.parametrize(
        ('direction', 'initial', 'final'), [
            (Direction.north(), Coordinates(3, 3), Coordinates(3, 2)),
            (Direction.south(), Coordinates(3, 3), Coordinates(3, 4)),
            (Direction.east(), Coordinates(3, 3), Coordinates(4, 3)),
            (Direction.west(), Coordinates(3, 3), Coordinates(2, 3)),
        ],
    )
    def test_moves_forward(
            self,
            direction: Direction,
            initial: Coordinates,
            final: Coordinates,
    ) -> None:
        rover = Rover(initial, direction)
        rover.move_forward()
        assert rover.position() == final

    @pytest.mark.parametrize(
        ('direction', 'initial', 'final'), [
            (Direction.north(), Coordinates(3, 3), Coordinates(3, 4)),
            (Direction.south(), Coordinates(3, 3), Coordinates(3, 2)),
            (Direction.east(), Coordinates(3, 3), Coordinates(2, 3)),
            (Direction.west(), Coordinates(3, 3), Coordinates(4, 3)),
        ],
    )
    def test_moves_backward(
            self,
            direction: Direction,
            initial: Coordinates,
            final: Coordinates,
    ) -> None:
        rover = Rover(initial, direction)
        rover.move_backward()
        assert rover.position() == final

    @pytest.mark.parametrize(
        ('initial', 'final'), [
            (Direction.north(), Direction.east()),
            (Direction.east(), Direction.south()),
            (Direction.south(), Direction.west()),
            (Direction.west(), Direction.north()),
        ],
    )
    def test_turns_right(self, initial: Direction, final: Direction) -> None:
        rover = Rover(Coordinates(3, 3), initial)
        rover.turn_right()
        assert rover.direction() == final

    @pytest.mark.parametrize(
        ('initial', 'final'), [
            (Direction.north(), Direction.west()),
            (Direction.west(), Direction.south()),
            (Direction.south(), Direction.east()),
            (Direction.east(), Direction.north()),
        ],
    )
    def test_turns_left(self, initial: Direction, final: Direction) -> None:
        rover = Rover(Coordinates(3, 3), initial)
        rover.turn_left()
        assert rover.direction() == final


class TestCoordinates:

    def test_two_equal_coordinates(self) -> None:
        assert Coordinates(0, 0) == Coordinates(0, 0)

    def test_two_coordinates_with_differrent_horizontal_position(self) -> None:
        assert Coordinates(0, 0) != Coordinates(1, 0)

    def test_two_coordinates_with_differrent_vertical_position(self) -> None:
        assert Coordinates(0, 0) != Coordinates(0, 1)


class TestDirection:

    def test_two_equal_directions(self) -> None:
        assert Direction.north() == Direction.north()

    def test_two_differernt_directions(self) -> None:
        assert Direction.north() != Direction.south()
