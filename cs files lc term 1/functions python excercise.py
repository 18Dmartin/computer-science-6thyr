#q1
"""
def fun1():
    x = int(input("what is you number"))
    return x
l = fun1()

def fun2():
    y = 0
    while y <= l:
        print(y)
        y = y + 1
    return
fun2()

#q2
""
def fun3():
    x = int(input("choose ur high number"))
    y = int(input("choose ur low number"))
    z = x>=y
    
    print(v)
    return
fun3()
"""
num1 = int(input("1) Addition \n2) subtraction \nenter 1 or 2:"))
def add1():
    import random
    rand1 = (random.randrange(5, 20, 2))
    rand2 = (random.randrange(5, 20, 2))
    return rand1 and rand2
r1 = add1()
r2 = add1()
truanwr = r1 + r2
print(r1 , r2)
if num1 == 1:
    add1()
    anwr1 = int(input("what is the answer if you add both numbers together"))
    if (r1 + r2) == anwr1:
        print("your answer was", anwr1)
        print("the correct answer was", truanwr)
        
    elif (r1 + r2) != anwr1:
        print("your answer was", anwr1)
        print("the correct answer was", truanwr)


""