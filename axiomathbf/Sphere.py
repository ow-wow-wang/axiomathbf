from sympy import *


class Sphere(Circle):
    def __init__(self, center=Point(0, 0, 0), radius=1, eq=None):
        self.center = center
        self.radius = radius
        self.eq = eq
        self.__x, self.__y, self.__z = symbols("x y z")

    def getCenter(self):
        if eq:
            return 
        return self.center

    def getRadius(self):
        if eq:
            return
        return self.radius

    def getEquation(self):
        return (self.__x-self.center.x) + (self.__y-self.center.y) + \
            (self.__z-self.center.z) - radius**2

    def isPointInSphere(self, point):
        c1, c2, c3 = self.center
        checkZero = self.getEquation().subs(
            [(self.__x, c1), (self.__y, c2), (self.__z, c3)])
        return checkZero == 0

    def completeTheSquare(self, n):
        return (n/2)**2

    def formatEquation(self):
        eq = self.eq.as_coefficients_dict()
        for squaredVar in [self.__x**2, self.__y**2, self.__z**2]:
            coeff = eq[squaredVar]
            if coeff != 1:
                for key in eq:
                    eq[key] /= eq[squaredVar]
                break
        completedSquare = [-self.completeTheSquare(
            var) for var in [self.__x, self.__y, self.__z]]

        constant = eq[1] + sum(completedSquare)
        return (self.__x+completedSquare[0]/2)**2 + \
            (self.__y+completedSquare[1]/2)**2 + \
            (self.__z-completedSquare[2]/2)**2

    def __str__(self):
        return str(self.getEquation())

    def setCenter(self, center):
        self.center = center

    def setRadius(self, radius):
        self.radius = radius

    def setEquation(self, eq):
        self.eq = eq


if __name__ == "__main__":
    pass
