class CharacterCount:
    def __init__(self):
        self.var = ""

    def set_var(self, string):
        if type(string) == int:
            print("Invalid input.")
        else:
            self.var = string

    def get_count(self):
        occurence = 0
        for i in self.var:
            occurence = occurence + 1
        return occurence


char = CharacterCount()

char.set_var("123")
count = char.get_count()
print("Count of character is : ", count)
