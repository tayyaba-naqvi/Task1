char = input("Enter an alphabet : ")

if char.__len__() == 1:
    if 'A' <= char <= 'Z':
        if char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U':
            print("It is a vowel")
        else:
            print("It is a consonant")
    elif 'a' <= char <= 'z':
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
            print("It is a vowel")
        else:
            print("It is a consonant")
    else:
        print("your input is invalid")
else:
    print("Too many characters")
