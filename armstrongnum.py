num = int(input("Enter the number : "))

sum = 0
temp = num

while(temp>0):
    digit = temp % 10
    cude = digit ** 3
    sum = sum + cude
    temp //=10

if sum == num:
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")