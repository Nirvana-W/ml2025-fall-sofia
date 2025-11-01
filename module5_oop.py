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


def main():
    N = int(input("Enter the number of elements (N): "))

    num_list = NumberList()

    for i in range(N):
        num = int(input(f"Enter number {i + 1}: "))
        num_list.insert_number(num)

    X = int(input("Enter the number to search for: "))

    result = num_list.search_number(X)
    print(result)


if __name__ == "__main__":
    main()
