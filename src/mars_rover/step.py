class Step:

    @classmethod
    def north(cls) -> 'Step':
        return cls(0, -1)

    @classmethod
    def south(cls) -> 'Step':
        return cls(0, 1)

    @classmethod
    def east(cls) -> 'Step':
        return cls(1, 0)

    @classmethod
    def west(cls) -> 'Step':
        return cls(-1, 0)

    def __init__(self, east: int, south: int) -> None:
        self._east = east
        self._south = south

    def points_south(self) -> int:
        return self._south

    def points_east(self) -> int:
        return self._east
