def openFile(fileName):
    return list(open(fileName, "r"))


def create_voting_dic(strlist):
    votingDic = {}

    for a in strlist:
        lst = a.strip("\n").split()
        for i in range(3, len(lst)):
            lst[i] = int(lst[i])

        votingDic[lst[0]] = lst[3:]

    return votingDic


def policy_compare(sent_a, sent_b, voting_dict):
    return dotProduct(voting_dict[sent_a], voting_dict[sent_b])


def most_similar(sen, voting_dict):
    mostSimilar = ""
    mostSimilarTrack = 0

    for i in voting_dict.keys():
        if i != sen and dotProduct(voting_dict[sen], voting_dict[i]) > mostSimilarTrack:
            mostSimilar = i
            mostSimilarTrack = dotProduct(voting_dict[sen], voting_dict[i])

    return mostSimilar


def least_similar(sen, voting_dict):
    leastSimilar = ""
    leastSimilarTrack = len(voting_dict[sen])

    for i in voting_dict.keys():
        if i != sen and dotProduct(voting_dict[sen], voting_dict[i]) < leastSimilarTrack:
            leastSimilar = i
            leastSimilarTrack = dotProduct(voting_dict[sen], voting_dict[i])

    return leastSimilar


def find_average_similarity(sen, sen_set, voting_dict):
    return sum(dotProduct(voting_dict[sen], voting_dict[x]) for x in sen_set)/len(sen_set)


def find_average_record(sen_set, voting_dict):
    subDict = {k : voting_dict[k] for k in voting_dict.keys() if k in sen_set}
    avgLst = []

    for i in range(len(subDict[sen_set[0]])):
        sumVal = 0
        for k in subDict.keys():
            sumVal += subDict[k][i]
        avgLst.append(sumVal/len(subDict.keys()))

    return avgLst

def bitter_rivals(voting_dict):
    leastNames = []
    least = 10000
    for i in voting_dict.keys():
        for j in voting_dict.keys():
            if dotProduct(voting_dict[i], voting_dict[j]) < least:
                leastNames = [i, j]
                least = dotProduct(voting_dict[i], voting_dict[j])

    return leastNames

def dotProduct(vectorA, vectorB):
    return sum(vectorA[i] * vectorB[i] for i in range(len(vectorA)))


votingDict = create_voting_dic(openFile("voting_record_dump109.txt"))
print(policy_compare("Pryor", "Obama", votingDict))
print(most_similar("Chafee", votingDict))
print(least_similar("Santorum", votingDict))
print(find_average_record(["Chafee", "Santorum"], votingDict))
print(bitter_rivals(votingDict))