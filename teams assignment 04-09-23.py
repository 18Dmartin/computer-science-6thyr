#1
runningTotal = 0
Price1 = 12
runningTotal = runningTotal + Price1
Price2 = 24
runningTotal = runningTotal + Price2
Price3 = 36
runningTotal = runningTotal + Price3
Price4 = 48
runningTotal = runningTotal + Price4
print ("the running total is", runningTotal)

#2
fin1 = open("daffodils.txt")
totalLines = 0 
print(fin1)
for line in fin1:
    print(line.strip())
    totalLines= totalLines + 1
    
print(totalLines)

#3


fin2 = open("num_calc_1.txt")
Totalnum = 0
Totallines2 = 0
for line in fin2:
    line = line.strip()
    if(line.isdigit()):
        x = int(line)
        Totallines2 = Totallines2 + 1
        Totalnum = Totalnum + x
fin2.close()

fin3 = open("num_calc_2.txt")
Totalnum2 = 0
Totallines3 = 0
for line in fin3:
    line = line.strip()
    if(line.isdigit()):
        y = int(line)
        Totallines3 = Totallines3 + 1
        Totalnum2 = Totalnum2 + y
fin3.close()


Totallinestg = Totallines3 + Totallines2
Totalmean = (Totalnum + Totalnum2) / Totallinestg
print(Totallinestg,"  is the combined lines")
print((Totalnum + Totalnum2),"  is the both nums added")


print(Totalmean,"  is the mean")

#4

usertotalnum = 0
useramount = 0
usernum = 0
print("please input 20 numbers")
while useramount != 20:
    usernum = int(input("please input a number"))
    usertotalnum = usertotalnum +usernum
    useramount = useramount + 1
    usernum = 0 
    usernum = int(input("please input a number "))
    
mean1 = usertotalnum / useramount
print(usertotalnum, "is the total amount")
print(useramount, "is the total amount of numbers")
print(mean1,"  is the mean")

print(usertotalnum, "is the total amount")


#5
useramount1 = 0
usernum = 0
fin5 = open("teams assignment 04-09-23.txt",'w')
while useramount1 != 10:
    usernum1 = str(input("please input a number"))
    useramount1 = useramount1 + 1
    fin5.write(usernum1)
    fin5.write("\n")
    
fin5.close()


fin5 = open("teams assignment 04-09-23.txt")
Totallines5 = 0 
Totalnum2 = 0
for line in fin5:
    line = line.strip()
    if(line.isdigit()):
        z = int(line)
        Totallines5 = Totallines5 + 1
        Totalnum2 = Totalnum2 + z
fin2.close()
mean2 = Totalnum2 / Totallines5
print(mean2,"  is the mean")