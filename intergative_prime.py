lower = int(input("Enter the lower bound of the range: "))
upper = int(input("Enter the upper bound of the range: "))

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
