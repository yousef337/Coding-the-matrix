from mat import Mat
import matutil
from vec import Vec
from GF2 import one

#4.14.1
gMatrix = matutil.listlist2mat([[one,0,one,one],[one,one,0,one],[0,0,0,one],[one,one,one,0],[0,0,one,0],[0,one,0,0],[one,0,0,0]])
#4.14.2
vecMsg = Vec({0, 1, 2, 3}, {0:one,3:one})
encodedMsg = gMatrix * vecMsg
print(encodedMsg.f)
#4.14.3

# Testing my answer, [0, 0, 1, 1]
vecMsg = Vec({0, 1, 2, 3}, {2:one,3:one})
encodedMsg = gMatrix * vecMsg
print(encodedMsg.f)

# Testing the R matrix. RG = I. Apparently, since the G is not a square matrix, there is no inverse for it. However, there
# could be left or right inverse. This R is the right inverse of G

rMAt = Mat(({0,1,2,3},{0,1,2,3,4,5,6}),{(1,0):0,(0,6):one,(1,5): one,(2,4) : one,(3,2) : one})

#4.14.4
hMAt = Mat(({0,1,2},{0,1,2,3,4,5,6}), {(0,3):one,(0,4):one,(0,5):one,(0,6):one, (1,1):one,(1,2):one,(1,5):one,(1,6):one,(2,0):one,(2,2):one,(2,4):one,(2,6):one})
print(hMAt*gMatrix)