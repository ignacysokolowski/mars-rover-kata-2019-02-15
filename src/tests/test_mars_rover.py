import pytest

from mars_rover import Direction
from mars_rover import Location
from mars_rover import Rover


class TestRover:

    def test_starts_at_the_given_position_and_facing_direction(self) -> None:
        rover = Rover(Location(1, 3), Direction.north())
        assert rover.position() == Location(1, 3)
        assert rover.direction() == Direction.north()

    @pytest.mark.parametrize(
        ('direction', 'initial', 'final'), [
            (Direction.north(), Location(3, 3), Location(3, 2)),
            (Direction.south(), Location(3, 3), Location(3, 4)),
            (Direction.east(), Location(3, 3), Location(4, 3)),
            (Direction.west(), Location(3, 3), Location(2, 3)),
        ],
    )
    def test_moves_forward(
            self,
            direction: Direction,
            initial: Location,
            final: Location,
    ) -> None:
        rover = Rover(initial, direction)
        rover.move_forward()
        assert rover.position() == final

    def test_moves_backward_south_when_facing_north(self) -> None:
        rover = Rover(Location(3, 3), Direction.north())
        rover.move_backward()
        assert rover.position() == Location(3, 4)

    def test_moves_backward_north_when_facing_south(self) -> None:
        rover = Rover(Location(3, 3), Direction.south())
        rover.move_backward()
        assert rover.position() == Location(3, 2)

    def test_moves_backward_west_when_facing_east(self) -> None:
        rover = Rover(Location(3, 3), Direction.east())
        rover.move_backward()
        assert rover.position() == Location(2, 3)

    def test_moves_backward_east_when_facing_west(self) -> None:
        rover = Rover(Location(3, 3), Direction.west())
        rover.move_backward()
        assert rover.position() == Location(4, 3)

    @pytest.mark.parametrize(
        ('initial', 'final'), [
            (Direction.north(), Direction.east()),
            (Direction.east(), Direction.south()),
            (Direction.south(), Direction.west()),
            (Direction.west(), Direction.north()),
        ],
    )
    def test_turns_right(self, initial: Direction, final: Direction) -> None:
        rover = Rover(Location(3, 3), initial)
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
        rover = Rover(Location(3, 3), initial)
        rover.turn_left()
        assert rover.direction() == final


class TestLocation:

    def test_two_equal_locations(self) -> None:
        assert Location(0, 0) == Location(0, 0)

    def test_two_locations_with_differrent_horizontal_position(self) -> None:
        assert Location(0, 0) != Location(1, 0)

    def test_two_locations_with_differrent_vertical_position(self) -> None:
        assert Location(0, 0) != Location(0, 1)


class TestDirection:

    def test_two_equal_directions(self) -> None:
        assert Direction.north() == Direction.north()

    def test_two_differernt_directions(self) -> None:
        assert Direction.north() != Direction.south()
