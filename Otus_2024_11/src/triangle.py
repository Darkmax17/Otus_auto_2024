class Triangle:
    def __init__(self, side_a, side_b, side_c):
        # Проверка, что все стороны переданы (не None)
        if side_a is None or side_b is None or side_c is None:
            raise ValueError("Должны быть переданы все три стороны треугольника")

        # Проверка, что все стороны больше 0
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("Стороны треугольника должны быть больше 0")

        # Проверка на корректность треугольника (сумма двух сторон должна быть больше третьей)
        if (side_a + side_b <= side_c) or (side_b + side_c <= side_a) or (side_c + side_a <= side_b):
            raise ValueError("Треугольник с такими сторонами не существует")

        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @property
    def area(self):
        # Реализация вычисления площади (например, по формуле Герона)
        s = (self.side_a + self.side_b + self.side_c) / 2
        return (s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c)) ** 0.5

    @property
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

    def add_area(self, other):
        if not hasattr(other, 'area'):
            raise ValueError("Переданный объект не имеет метода area")
        return self.area + other.area