range_num = int(input("Enter a number to divide by another number: "))
divisor = int(input("Enter the divisor: "))

for i in range(1, range_num + 1):
    if i % divisor == 0:
        print(f"{i} is divisible by {divisor}")
    else:
        print(f"{i} is not divisible by {divisor}")