import math

class Tetrahedron:
    def __init__(self, edge: float):
        """Устанавливает длину ребра."""
        self.edge = float(edge)
    
    def surface(self) -> float:
        """Вычисляет площадь поверхности тетраэдра."""
        return math.sqrt(3) * (self.edge ** 2)
    
    def volume(self) -> float:
        """Вычисляет объём тетраэдра."""
        return (self.edge ** 3) / (6 * math.sqrt(2))

#Тест
#t1 = Tetrahedron(5)
#Длина ребра: 5.0
#Площадь поверхности: 43.30127018922193
#Объём: 14.731391274719739

# Изменение длины ребра
#t1.edge = 6
#Обновлённая длина ребра: 6
#Обновлённая площадь поверхности: 62.35382907247958
