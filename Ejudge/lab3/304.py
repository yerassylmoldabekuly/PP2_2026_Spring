class StringHandler:

    def getString(self, s):
        self.s = s

    def printString(self):
        return self.s.upper()

word = input()
s = StringHandler()
s.getString(word)
print(s.printString())