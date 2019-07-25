num = input("Enter an integer : ")

for char in num:
    if char <= '0' or char >= '9':
        print("Your input is invalid")
        break
else:
    num=int(num)
    print("The computational result is : ", num + num * num + num * num * num)
