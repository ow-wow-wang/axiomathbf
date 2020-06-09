import pytest
from axiomathbf.Sphere import Sphere
from sympy import symbols

x, y, z = symbols("x y z")


def test_format_equation1():
    sphere1 = Sphere(eq=4*x**2 + 4*y**2 - 16*x - 24*y + 51)
    sphere2 = Sphere(eq=z**2 + (x - 2)**2 + (y - 3)**2 - 1/4)
    assert sphere1 == sphere2


def test_format_equation2():
    sphere1 = Sphere(eq=100*x**2+100*y**2-100*x+240*y-56)
    pass


def test_format_equation3():
    pass


def test_format_equation4():
    pass


def test_format_equation5():
    pass


def test_format_equation6():
    pass

def test_get_center1():
    pass

def test_get_radius1():
    pass

def test_get_radius_and_center1():
    pass

def test_get_radius_and_center2():
    pass

def test_get_radius_and_center3():
    pass