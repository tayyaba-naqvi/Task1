
def min_num_in_list(list):
    min = list[0]
    for i in list:
        if (i < min):
            min = i
    return min

def second_smallest(list):
    firstMin = min_num_in_list(list)
    secondMin = list[0]
    for i in list:
        if ((i < secondMin) and (i != firstMin)):
            secondMin = i
    return secondMin


list = [5, 2, 3, 4, 5,1,0,8,6,4,-2,-10]
min = second_smallest(list)
print("Second smallest number is : ",min)