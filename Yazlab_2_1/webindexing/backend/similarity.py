from numpy.linalg import norm
from numpy import dot


def calculateSimilarity(list1, list2):
    vector1 = []
    vector2 = []
    list1words = []
    list2Words = []
    for x in list2:
        list2Words.append(x[0])

    for x in list1:
        list1words.append(x[0])
    
    for value in list1:
        vector1.append(value[1])

    for k in list1words:
        if k in list2Words:
            print("true")
            vector2.append(value[1])
        else:
            vector2.append(0)
    return dot(vector1, vector2)/(norm(vector1)*norm(vector2))
