class NumberList:
    def __init__(self):
        self.numbers = []

    def insert_number(self, num):
        self.numbers.append(num)

    def search_number(self, x):
        if x in self.numbers:
            return self.numbers.index(x) + 1
        else:
            return -1
