class Pupil:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Name: {self.x}, Age: {self.y}"

    def __add__(self, other):
        if isinstance(other, Pupil):
            return Pupil(self.x + other.x, self.y + other.y)

p1 = Pupil(2, 5)
p2 = Pupil(3, 10)

print(p1)
print(p2)

p3 = p1 + p2
print(p3)