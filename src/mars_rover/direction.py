import abc

from .step import Step


class Direction(abc.ABC):

    @classmethod
    def north(cls) -> 'Direction':
        return North()

    @classmethod
    def south(cls) -> 'Direction':
        return South()

    @classmethod
    def east(cls) -> 'Direction':
        return East()

    @classmethod
    def west(cls) -> 'Direction':
        return West()

    @abc.abstractmethod
    def opposite(self) -> 'Direction':
        ...

    @abc.abstractmethod
    def next_to_the_right(self) -> 'Direction':
        ...

    @abc.abstractmethod
    def next_to_the_left(self) -> 'Direction':
        ...

    @abc.abstractmethod
    def step(self) -> Step:
        ...

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}()'

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Direction):  # pragma: nocover
            return NotImplemented
        return type(self) == type(other)


class North(Direction):

    def opposite(self) -> Direction:
        return Direction.south()

    def next_to_the_right(self) -> Direction:
        return Direction.east()

    def next_to_the_left(self) -> Direction:
        return Direction.west()

    def step(self) -> Step:
        return Step.north()


class South(Direction):

    def opposite(self) -> Direction:
        return Direction.north()

    def next_to_the_right(self) -> Direction:
        return Direction.west()

    def next_to_the_left(self) -> Direction:
        return Direction.east()

    def step(self) -> Step:
        return Step.south()


class East(Direction):

    def opposite(self) -> Direction:
        return Direction.west()

    def next_to_the_right(self) -> Direction:
        return Direction.south()

    def next_to_the_left(self) -> Direction:
        return Direction.north()

    def step(self) -> Step:
        return Step.east()


class West(Direction):

    def opposite(self) -> Direction:
        return Direction.east()

    def next_to_the_right(self) -> Direction:
        return Direction.north()

    def next_to_the_left(self) -> Direction:
        return Direction.south()

    def step(self) -> Step:
        return Step.west()
