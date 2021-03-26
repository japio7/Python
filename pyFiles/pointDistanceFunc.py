def distance(lst) -> tuple:
    for i in lst:
        dist = abs(lst[n][0] - lst[n][1])
        newPair = (lst[n][0], lst[n][1], dist)
        newList.append(newPair)
        n+=1
    newList.sort(key = lambda tup: tup[2])
    shortestDist_0 = (newList[0][0], newList[0][1])
    shortestDist_1 = (newList[1][0], newList[1][1])

    result = ((shortestDist_0), (shortestDist_1))

    return result

lstTups = [(8, 21), (12, 19), (7, 38), (9, 23), (2, 7), (31, 15), (22, 9)]

print(distance(lstTups))
