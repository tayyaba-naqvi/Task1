str=input("Enter a string : ")
countNo=0
countLetters=0
for character in str:
    if((character >= 'A' and character <= 'Z') or (character >= 'a' and character <= 'z')):
        countLetters=countLetters+1
    elif(character >= '0' and character <= '9'):
        countNo=countNo+1
    else:
        pass

print("No of alphabets : ",countLetters)
print("No of digits : ", countNo)
