def min_num_in_list(list):
    min = list[0]
    for i in list:
        if (i < min):
            min = i
    return min


list = [5, 2, 3, 4, 5,1,0,-8,6,4,-2,-10]
min = min_num_in_list(list)
print("Minimum number is : ",min)
