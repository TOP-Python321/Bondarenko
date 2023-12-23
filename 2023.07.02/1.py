from math import sqrt
from dataclasses import dataclass
@dataclass
class Tetrahedron:
    """
    Описывает правильный тетраэдр.
    """
    def __init__(self, edge: float):
        self.edge = float(edge)

    def surface(self) -> float:
        """ Вычисление площади """
        square = sqrt(3) * self.edge ** 2
        return square

    def volume(self) -> float:
        """ Вычисление обьема """
        vol = (self.edge ** 3) / 12 * sqrt(2)
        return vol

#  >>> t1 = Tetrahedron(5)
#  >>> t1.edge
#  5.0
#  >>> t1.surface()
#  43.30127018922193
#  >>> t1.volume()
#  14.731391274719739
#  >>>
#  >>> t1.edge = 6
#  >>> t1.surface()
#  62.35382907247958
