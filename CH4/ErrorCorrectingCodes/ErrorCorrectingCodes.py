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
