"""
#TODO INCOMPLETE & TEST THE CLASS
The issue is the slow of the computation on my local machine due to the image's size
"""
import sys

sys.path.insert(0, '/Users/yousefaltaher/Documents/GitHub/Coding-the-matrix/CH4/ErrorCorrectingCodes')
sys.path.insert(0, '/Users/yousefaltaher/Documents/GitHub/Coding-the-matrix/CH4/2DGeometryTransformation')

from vec import Vec
import image_mat_util as imu
import matutil
import transform as tf
from mat import Mat


def move2board(y):
    return Vec({"y1", "y2", "y3"},
               {"y1": y.getitem("y1") / y.getitem("y3"), "y2": y.getitem("y2") / y.getitem("y3"), "y3": 1})


def make_equations(x1, x2, w1, w2):
    u = Vec({0, 1, 2, 3, 4, 5, 6, 7, 8}, {0: w1 * x1, 1: w1 * x2, 2: w1, 3: -x1, 4: -x2, 5: -1})
    v = Vec({0, 1, 2, 3, 4, 5, 6, 7, 8}, {0: w2 * x1, 1: w2 * x2, 2: w2, 6: -x1, 7: -x2, 8: -1})

    return [u, v]


# 5.12.13
w = Vec({0, 1, 2, 3, 4, 5, 6, 7, 8}, {3: 1})

# 5.12.14

x1 = make_equations(358, 36, 0, 0)
x2 = make_equations(329, 597, 1, 0)
x3 = make_equations(592, 157, 0, 1)
x4 = make_equations(580, 483, 1, 1)
lstVec = x1+x2+x3+x4+[w]
L = matutil.rowdict2mat(lstVec)
b = Vec({0, 1, 2, 3, 4, 5, 6, 7, 8}, {8: 1})

H = Mat(({"x1", "x2", "x3"},{"x1", "x2", "x3"}), {(0,0):10697714712404092/5653420829218085,(0,1):6836671238/223111442015, (0,2):-9920365941044093000/5653420829218085,(1,0):1,(1,1):-234/121, (1,2):-34894/121, (2,0):-1321512/504185, (2,1):-751448/5546035, (2,2):5231166384/5546035})

(X_pts, colors) = imu.file2mat("board.png",("x1","x2","x3"))
print(H)
print(X_pts)
Y_pts = H*X_pts

def mat_move2board(Y_pts):
    return Mat((Y_pts.D[0], Y_pts.D[1]),
               {(y, x): Vec.__getitem__(move2board(matutil.mat2coldict(Y_pts)[x]), y) for x in Y_pts.D[1] for y in range(3)})


Y_board = mat_move2board(Y_pts)