class CharacterCount:
    __var = ""

    def __init__(self):
        __var = ""

    def __isnumber(self,val):
        for i in val:
            if(i <= '0' or i>= '9'):
                return False
        return True

    def setVar(self, str):
        if(self.__isnumber(str)):
            print("You have enetered an integer")
        else:
            self.__var = str

    def getCount(self):
        count=0
        for i in self.__var:
            count=count+1
        return count

char=CharacterCount()

char.setVar(input("Enter character : "))
count=char.getCount()
print("Count of characer is : " , count)
