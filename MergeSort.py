import operator

def compare(tuple1,tuple2):
    return int(tuple1[0][1] - tuple2[0][1])


def merge(left,right,compare):
    result=[]
    i,j=0,0

    while i<len(left) and j<len(right):
        if compare(left,right) <= 0:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

        for x in range(i, len(left)):
            result.append(left[x])
        for x in range(j, len(right)):
            result.append(right[x])

        return result


def mergeSort(aList,compare):
    if len(aList)<2:
        return aList[:]
    else:
        middle =len(aList)//2
        left =mergeSort(aList[:middle], compare)
        right=mergeSort(aList[middle:], compare)
        return merge(left,right,compare)

#------------------------------------------------------------------------
list1 = [["t3",72],("t1",54),("t2",68),("t4",89),("t5",73),("t6",73)]
list2 = [2,4,15,49,80,99]
list3 = [5,73,1,903,50,7,7,32]

result = mergeSort(list1, compare)



