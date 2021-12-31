import sys

sys.path.insert(0, '/Users/yousefaltaher/Documents/GitHub/Coding-the-matrix/CH4/ErrorCorrectingCodes')
from mat import Mat
import math


def identity():
    return Mat(({"x", "y", "u"}, {"x", "y", "u"}), {("x", "x"): 1, ("y", "y"): 1, ("u", "u"): 1})


def translation(alpha, beta):
    return Mat(({"x", "y", "u"}, {"x", "y", "u"}),
               {("x", "x"): 1, ("x", "u"): alpha, ("y", "y"): 1, ("y", "u"): beta, ("u", "u"): 1})


def scale(alpha, beta):
    return Mat(({"x", "y", "u"}, {"x", "y", "u"}),
               {("x", "x"): alpha, ("y", "y"): beta, ("u", "u"): 1})


def rotation(theta):
    return Mat(({"x", "y", "u"}, {"x", "y", "u"}),
               {("x", "x"): math.cos(theta), ("x", "y"): -math.sin(theta), ("y", "x"): math.sin(theta),
                ("y", "y"): math.cos(theta), ("u", "u"): 1})


def rotation_about(theta, x, y):
    return translation(x, y) * rotation(theta) * translation(x, y)


def reflect_x():
    return Mat(({"x", "y", "u"}, {"x", "y", "u"}),
               {("x", "x"): 1, ("y", "y"): -1, ("u", "u"): 1})


def reflect_y():
    return Mat(({"x", "y", "u"}, {"x", "y", "u"}),
               {("x", "x"): -1, ("y", "y"): 1, ("u", "u"): 1})


def scale_color(r, g, b):
    return Mat(({"r", "b", "g"}, {"r", "b", "g"}),
               {("r", "r"): r, ("b", "b"): b, ("g", "g"): g})


def grayscale():
    return scale_color(77/256, 151/256, 28/256)


def reflect_about(x1, y1, x2, y2):
    return reflect_x()*translation(0, -y1)*rotation(math.atan((y2-y1)/(x2-x1)))

print(reflect_about(3,5,4,1))