import pytest
from src.Rectangle import Rectangle
from src.Square import Square
from src.Circle import Circle
from src.Triangle import Triangle


class Negative:
    pass


@pytest.mark.parametrize(("side_a", "side_b"), [(7, 28), (3.12, 12.48)],
                         ids=['integer', 'float'])
def test_square_rectangle_add_area(side_a, side_b):
    s = Square(side_a)
    r = Rectangle(side_a, side_b)
    square_area = s.area
    rectangle_area = r.area
    print(f'Сумма площадей равна: {square_area + rectangle_area}')
    assert s.add_area(r) == (square_area + rectangle_area), f'Расчет суммы площадей отличается от заданного значения'


@pytest.mark.parametrize(("side_a", "side_b", "side_c"), [(7, 28, 25), (3.12, 12.48, 10.19)],
                         ids=['integer', 'float'])
def test_triangle_circle_add_area(side_a, side_b, side_c):
    t = Triangle(side_a, side_b, side_c)
    c = Circle(side_c)
    triangle_area = t.area
    circle_area = c.area
    print(f'Сумма площадей равна: {triangle_area + circle_area}')
    assert t.add_area(c) == (triangle_area + circle_area), f'Расчет суммы площадей отличается от заданного значения'


def test_sides_negative():
    with pytest.raises(ValueError, match='Диапазон атрибутов должен быть > 0'):
        r = Rectangle(0, -2)



def test_figure_negative():
    with pytest.raises(ValueError):
        c = Circle(5)
        n = Negative()
        c.add_area(n)