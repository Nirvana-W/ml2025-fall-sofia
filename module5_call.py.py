from module5_mod import NumberList

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