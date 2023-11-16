"""
list1 = [2,4,6,798,3244,465,7678,24,67]
def fun1(y):
    i = 0
    x = 0
    while i != len(list1):
        print(list1[x])
        if y == list1[x]:
            print("yes")
            return x
        i = i + 1
        x = x + 1
    return -1    
print(fun1(32454))
"""
userinput = int(input("input ur item"))
list2 = [2,4,7986,798,3244,465,7678,24,67]
list2.sort()
def funt2():
    length = len(list2)
    low = 0
    high = length-1
    q = 0
    mid = (low + high)//2
    while q != length:
        q = q + 1
        if userinput == list2[mid]:
             print ("yes")
        elif userinput < list2[mid]:
            low = mid + 1
            
print(funt2())