while True:
    N = int(input("Enter a positive integer N: "))
    if N > 0:
        break
    else:
        print("N must be positive, try again")


numbers = []
for i in range(N):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

X = int(input("Enter the number X to find: "))

if X in numbers:
    print(numbers.index(X) + 1)
else:
    print(-1)
