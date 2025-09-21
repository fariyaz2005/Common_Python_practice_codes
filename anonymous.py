terms = int(input("Enter the number of terms: "))
result = list(map(lambda x: x**2, range(terms+1)))
print(result)

for i in range(terms+1):
    print("the value of 2 raised to the power", i, "is",result[i])