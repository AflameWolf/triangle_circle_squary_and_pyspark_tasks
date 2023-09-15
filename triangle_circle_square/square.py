from  math import pi


class Square():
    def __init__(self,Square,right_triangle=None):
        self.square = Square
        self._right_triangle=right_triangle

    def __str__(self):
        if self._right_triangle:
            return f"{self.square},Right triangle:{self._right_triangle}"
        else:
            return f"Square: {self.square}"
    @staticmethod
    def triangle(a,b,c):
        """Вычисление площади треугольника и проверка на прямоугольность"""
        tian=[a,b,c]
        tian.sort(reverse=True)
        if tian[0]**2==tian[1]**2+tian[2]**2:
            p=(tian[0]+tian[1]+tian[2])/2
            s=(p*(p-tian[0])*(p-tian[1])*(p-tian[2]))**(0.5)
            return Square(round(s,2),True)
        else:
            p=(tian[0]+tian[1]+tian[2])/2
            s=(p*(p-tian[0])*(p-tian[1])*(p-tian[2]))**(0.5)
            return Square(round(s,2))
    @staticmethod
    def circle(radius):
        return Square(round(radius**2*pi,2))

    @staticmethod
    def i_dont_know_what_this(*args):
        """Проверка на фигуру по количеству аргументов """
        if len(args)==1:
            return Square.circle(args[0])
        if len(args)==3:
            return Square.triangle(args[0],args[1],args[2])
        else:
            return "I don't know what it is either"
