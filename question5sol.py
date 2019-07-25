def min_num_in_list(nolist):
    minn = nolist[0]
    for i in nolist:
        if i < minn:
            minn = i
    return minn


listOfNo = [5, 2, 3, 4, 5, 1, 0, -8, 6, 4, -2, -10]
minimum = min_num_in_list(listOfNo)
print("Minimum number is : ", minimum)
