num =input("Enter an integer : ")
val=0
flag=False
for char in num:
    if(char <= '0' or char >= '9'):
        print("Your input is invalid")
        break
    val=val*10+int(char)

else:
    print("The computational result is : ", val+val*val+val*val*val)
