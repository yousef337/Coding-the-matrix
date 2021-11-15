# Yousef Altaher
# TODO optimization - reducing time complexity

def openFile(fileName):
    file = list(open(fileName, "r"))
    return file

"""
Time complexity: O(N^2)
"""
def makeInverseIndex(strList):
    inverseDic = {x: 0 for y in range(len(strList)) for x in strList[y].split()}

    for i in inverseDic.keys():
        numSet = set()
        for j in list(enumerate(strList)):
            if i in j[1]:
                numSet.add(j[0])
        inverseDic[i] = numSet

    return inverseDic

"""
Time complexity: O(N)
"""
def orSearch(inverseIndex, query):
    completeSet = set()

    for i in query:
        completeSet = completeSet.union(completeSet, inverseIndex[i])

    return completeSet


"""
Time complexity: O(N)
"""
def andSearch(inverseIndex, query):
    completeSet = set()

    for i in query:
        if completeSet != set():
            completeSet = completeSet.intersection(completeSet, inverseIndex[i])
        else:
            completeSet = completeSet.union(completeSet, inverseIndex[i])

    return completeSet


file = openFile("stories_big.txt")
inverseDic = makeInverseIndex(file)
print orSearch(inverseDic, ["Does", "She"])
print andSearch(inverseDic, ["Does", "She"])
