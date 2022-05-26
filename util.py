def extractListFromMatrixX(matrix, x):
    l = []

    for row in matrix:
        l.append(row[x])

    return l

def zipLists(*lists):
    zipped = []

    for index, list in enumerate(lists):
        for item in list:
            if len(zipped) > index:
                zipped[index].append(item)
            else:
                zipped.append([item])

    return zipped