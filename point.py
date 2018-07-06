class Point:
    x = 0
    y = 0

    def __init__(self, a, b):
        self.x = a
        self.y = b

    def __lt__(self, other):
        return self.x * self.y < other.x * other.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
