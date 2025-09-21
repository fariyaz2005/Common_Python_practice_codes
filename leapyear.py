year = int(input("ENter the year : "))
if (year % 400 == 0) and (year % 100 == 0):
    print("the year is leap year")
elif (year % 4 == 0) and (year % 100 != 0):
    print("the year is leap year")
else:
    print("not leap year")