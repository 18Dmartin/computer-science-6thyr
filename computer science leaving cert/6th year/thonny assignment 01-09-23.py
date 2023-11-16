##Q1
myfloatvalue = float(9.82)
print (type(myfloatvalue))
a = str(myfloatvalue)
print (a)
print (type(a))
b = int(myfloatvalue)
print (b)
print (type(b))

##Q2
##mytext = boo
##a = int(mytext)
##Traceback (most recent call last):
##File "<string>", line 12, in <module>
##NameError: name 'boo' is not defined

##Q3
year = input("Enter the current year")
yearnum = int(year)
age = int(input("What age will you be at the end of this year?"))
agenum = int(age)
print("You were born in", yearnum-agenum)
##Traceback (most recent call last):
##File "<string>", line 22, in <module>
##TypeError: unsupported operand type(s) for -: 'str' and 'int'

## a)print("2000"+18) - problem is that 2000 is in quotes
## b)print("2000"+str(18))## - the numbers will just combine to give you 200018

#10
totalbill = 0
marsbprice = 1
cokepri = 1.50
crispspri = .80
teapri = 2
panpri = 3.50

totalbill = totalbill + (marsbprice * 5)
totalbill = totalbill + (cokepri * 4)
totalbill = totalbill + (crispspri * 3)
totalbill = totalbill + (teapri * 2)
totalbill = totalbill + (panpri * 1)
print("total price is ",totalbill)

#11
number1 = int(input("enter first number"))
number2 = int(input("enter second number"))
sum = number1 + number2
print(number1, "+", number2, "=", sum)

#12
f = int(input("enter fahrenheit"))
c = (f - 32)*5/9
print(c)

#13
def zellers_algorithm(day, month, year):
    if month < 3:
        month += 12
        year -= 1

    d = day
    m = month
    y = year % 100
    c = year // 100

    w = (d + (13 * (m + 1)) // 5 + y + (y // 4) + (c // 4) - (2 * c)) % 7

    # Map the result to the corresponding day of the week
    days_of_week = ["0", "1", "2", "3", "4", "5", "6"]

    return days_of_week[w]

# Input date in the format (day, month, year)
day = int(input("Enter the day (1-31): "))
month = int(input("Enter the month (1-12): "))
year = int(input("Enter the year : "))

day_of_week = zellers_algorithm(day, month, year)
print("the day of the week is",days_of_week)


