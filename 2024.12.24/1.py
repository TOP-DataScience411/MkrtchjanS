from math import sqrt

class Point:
    """Класс для представления точки на двумерной плоскости."""
    def __init__(self, x: float, y: float):
        self._x = x
        self._y = y

    @property
    def x(self) -> float:
        return self._x

    @x.setter
    def x(self, value):
        raise TypeError("Координата x неизменяема")

    @property
    def y(self) -> float:
        return self._y

    @y.setter
    def y(self, value):
        raise TypeError("Координата y неизменяема")

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point):
            return NotImplemented
        return self._x == other.x and self._y == other.y

    def __repr__(self) -> str:
        return f"({self._x}, {self._y})"

class Line:
    """Класс для представления отрезка на двумерной плоскости."""

    def __init__(self, start: Point, end: Point):
        self._start = start
        self._end = end
        self._length = self._length_calc(start, end)

    @staticmethod
    def _length_calc(point1: Point, point2: Point) -> float:
        return sqrt((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2)

    @property
    def start(self) -> Point:
        return self._start

    @start.setter
    def start(self, value: Point):
        if not isinstance(value, Point):
            raise TypeError("Начальная точка должна быть экземпляром Point")
        self._start = value
        self._length = self._length_calc(self._start, self._end)

    @property
    def end(self) -> Point:
        return self._end

    @end.setter
    def end(self, value: Point):
        if not isinstance(value, Point):
            raise TypeError("Конечная точка должна быть экземпляром Point")
        self._end = value
        self._length = self._length_calc(self._start, self._end)

    @property
    def length(self) -> float:
        return self._length

    def __repr__(self) -> str:
        return f"{self.start}———{self.end}"

class Polygon:
    """Класс для представления многоугольника."""

    def __init__(self, side1: Line, side2: Line, side3: Line, *sides: Line):
        self.sides = [side1, side2, side3] + list(sides)
        if len(self.sides) < 3:
            raise ValueError("Многоугольник должен состоять минимум из трех сторон.")
        if not self._is_closed():
            raise ValueError("Многоугольник не замкнут.")

    @property
    def perimeter(self) -> float:
        return sum(side.length for side in self.sides)

    def _is_closed(self) -> bool:
        for i in range(len(self.sides)):
            current_end = self.sides[i].end
            next_start = self.sides[(i + 1) % len(self.sides)].start
            if current_end != next_start:
                return False
        return True

    def __repr__(self) -> str:
        return f"Polygon({', '.join(map(str, self.sides))})"

#точки
#point_a = Point(0, 0)
#point_b = Point(3, 0)
#point_c = Point(3, 4)
#point_d = Point(0, 4)

#отрезки
#line_ab = Line(point_a, point_b)
#line_bc = Line(point_b, point_c)
#line_cd = Line(point_c, point_d)
#line_da = Line(point_d, point_a)

#Корректный многоугольник (четырехугольник)
#polygon = Polygon(line_ab, line_bc, line_cd, line_da)
#Многоугольник: Polygon((0, 0)———(3, 0), (3, 0)———(3, 4), (3, 4)———(0, 4), (0, 4)———(0, 0))
#Периметр: 14.0

#Некорректный многоугольник
#wrong_polygon = Polygon(line_ab, line_bc, line_cd)
#Ошибка: Многоугольник не замкнут.


#Многоугольник из менее чем 3 сторон
#invalid_polygon = Polygon(line_ab, line_bc,  line_bc)
#Ошибка: Многоугольник не замкнут.

#Изменение координат точки
#point_a.x = 5
#Ошибка изменения координат: Координата x неизменяема

#Установка некорректного значения для начала отрезка
#line_ab.start = "Некорректная точка"
#Ошибка установки начала отрезка: Начальная точка должна быть экземпляром Point

#Установка некорректного значения для конца отрезка
#line_ab.end = 123
#Ошибка установки конца отрезка: Конечная точка должна быть экземпляром Point