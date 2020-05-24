class Position:
    def __str__(self) -> str:
        return "{}:{}".format(self.X, self.Y)

    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def __eq__(self, other) -> bool:
        return self.X == other.X and self.Y == other.Y
