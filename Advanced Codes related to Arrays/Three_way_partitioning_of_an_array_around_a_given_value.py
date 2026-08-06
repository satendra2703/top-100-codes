#Three way partitioning of an array around a given value in python ?
"""We are given an array and a range say [low, high], we need to partition the array in such a way,

All the elements less than low value, should come first.
Elements between the low and high value come in middle.
All elements greater than high should come at the last."""

def partition(arr, l, h):
    lm = []
    mm = []
    hm = []
    for i in arr:
        if i < l:
            lm.append(i)
        elif i > h:
            hm.append(i)
        else:
            mm.append(i)
    return lm + mm + hm


array = [1, 17, 22, 16, 13, 5, 43, 18, 3, 10]
lowVal = 14
highVal = 20
print("After Partitioning :", partition(array, lowVal, highVal))