class Position:
    def __str__(self) -> str:
        return "{}:{}".format(self.X, self.Y)

    def __init__(self, x, y):
        self.X = x % 10
        self.Y = y % 10
