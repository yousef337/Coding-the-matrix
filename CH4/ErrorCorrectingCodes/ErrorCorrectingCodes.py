from mat import Mat
import matutil
from vec import Vec
from GF2 import one

# 4.14.1
gMatrix = matutil.listlist2mat(
    [[one, 0, one, one], [one, one, 0, one], [0, 0, 0, one], [one, one, one, 0], [0, 0, one, 0], [0, one, 0, 0],
     [one, 0, 0, 0]])
# 4.14.2
vecMsg1 = Vec({0, 1, 2, 3}, {0: one, 3: one})
encodedMsg1 = gMatrix * vecMsg1
# print(encodedMsg1)
# 4.14.3

# Testing my answer, [0, 0, 1, 1]
vecMsg2 = Vec({0, 1, 2, 3}, {2: one, 3: one})
encodedMsg2 = gMatrix * vecMsg2
# print(encodedMsg2)

# Testing the R matrix. RG = I. Apparently, since the G is not a square matrix, there is no inverse for it. However, there
# could be left or right inverse. This R is the right inverse of G

rMAt = Mat(({0, 1, 2, 3}, {0, 1, 2, 3, 4, 5, 6}), {(1, 0): 0, (0, 6): one, (1, 5): one, (2, 4): one, (3, 2): one})

# 4.14.4
hMAt = Mat(({0, 1, 2}, {0, 1, 2, 3, 4, 5, 6}),
           {(0, 3): one, (0, 4): one, (0, 5): one, (0, 6): one, (1, 1): one, (1, 2): one, (1, 5): one, (1, 6): one,
            (2, 0): one, (2, 2): one, (2, 4): one, (2, 6): one})


# print(rMAt * gMatrix)


# 4.14.5

def find_error(errorSyndromeVec):
    # HC == HE -> hHC == hHe == e
    # couldn't compute h such that hH = I. I have
    # noticed that the errorSyndrome represents the
    # binary position of the error itself, and 0 if none
    # so, I have used this in this method until I
    # recognize a better method

    # change one, GF(2), to 1, R, in order to perform the *

    errorSyndromeVecOverR = errorSyndromeVec.copy()
    for a in errorSyndromeVecOverR.f.keys():
        errorSyndromeVecOverR.f[a] = 1 if errorSyndromeVecOverR.f[a] == one else 0

    binaryConv = Vec({0, 1, 2}, {0: 1, 1: 2, 2: 4})
    if binaryConv * errorSyndromeVecOverR == 0:
        return Vec({0, 1, 2, 3, 4, 5, 6}, {})
    return Vec({0, 1, 2, 3, 4, 5, 6},
               {(binaryConv * errorSyndromeVecOverR) - 1: one})  # -1 since 0 correspond to no error


# print(find_error(hMAt * encodedMsg2))

# 4.14.6

codedMessageRec = Vec({0, 1, 2, 3, 4, 5, 6}, {0: one, 2: one, 3: one, 5: one, 6: one})
print(rMAt * (find_error(hMAt * codedMessageRec) + codedMessageRec))


# 4.14.7

def find_error_matrix(s):
    # return Mat(s.D, {(x, y): Vec.__getitem__() for x})
    return Mat(({0, 1, 2, 3, 4, 5, 6}, s.D[1]),
               {(y, x): Vec.__getitem__(find_error(matutil.mat2coldict(s)[x]), y) for x in s.D[1] for y in range(7)})


print(find_error(matutil.mat2coldict(Mat(({0, 1, 2}, {0, 1}), {(0, 0): one, (1, 0): one, (2, 0): one, (2, 1): one}))[0]))
print(Mat(({0, 1, 2}, {0, 1}), {(0, 0): one, (1, 0): one, (2, 0): one, (2, 1): one}))
print(find_error_matrix(Mat(({0, 1, 2}, {0, 1}), {(0, 0): one, (1, 0): one, (2, 0): one, (2, 1): one})))
