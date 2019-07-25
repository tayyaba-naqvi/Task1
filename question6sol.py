def min_num_in_list(nolist):
    minn = nolist[0]
    for i in nolist:
        if i < minn:
            minn = i
    return minn


def second_smallest(nolist):
    first = min_num_in_list(nolist)
    second = nolist[0]
    for i in nolist:
        if (i < second) and (i != first):
            second = i
    return second


listOfNo = [5, 2, 3, 4, 5, 1, 0, 8, 6, 4, -2, -10]
minimum = second_smallest(listOfNo)
print("Second smallest number is : ", minimum)
