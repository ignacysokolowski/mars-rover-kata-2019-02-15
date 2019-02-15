from kata.mars_rover import Direction
from kata.mars_rover import Location
from kata.mars_rover import Rover


class TestRover:

    def test_starts_at_the_given_position_and_facing_direction(self) -> None:
        rover = Rover(Location(1, 3), Direction.north())
        assert rover.position() == Location(1, 3)
        assert rover.direction() == Direction.north()

    def test_moves_forward_north(self) -> None:
        rover = Rover(Location(3, 3), Direction.north())
        rover.move_forward()
        assert rover.position() == Location(3, 2)

    def test_moves_forward_south(self) -> None:
        rover = Rover(Location(3, 3), Direction.south())
        rover.move_forward()
        assert rover.position() == Location(3, 4)

    def test_moves_forward_east(self) -> None:
        rover = Rover(Location(3, 3), Direction.east())
        rover.move_forward()
        assert rover.position() == Location(4, 3)

    def test_moves_forward_west(self) -> None:
        rover = Rover(Location(3, 3), Direction.west())
        rover.move_forward()
        assert rover.position() == Location(2, 3)

    def test_moves_backward_south_when_facing_north(self) -> None:
        rover = Rover(Location(3, 3), Direction.north())
        rover.move_backward()
        assert rover.position() == Location(3, 4)


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
