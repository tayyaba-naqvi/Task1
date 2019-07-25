str = input("Enter a string : ")
countNo = 0
countLetters = 0
for character in str:
    if 'A' <= character <= 'Z' or 'a' <= character <= 'z':
        countLetters = countLetters + 1
    elif '0' <= character <= '9':
        countNo = countNo + 1
    else:
        pass
print("No of alphabets : ", countLetters)
print("No of digits : ", countNo)
