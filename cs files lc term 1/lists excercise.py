#lists excercise

#q1
sports = []
sports1 = input("what is your first sport: ")
sports2 = input("what is your second sport: ")
sports.insert(0,sports1)
sports.insert(1,sports2)
print(sports)

#q2
subjects = ["english","irish","maths","spanish","french","biology"]
print(subjects)
whichdelete = input("what would you like to delete: ")
if whichdelete == "english" or "irish" or "maths"or "spanish" or "french" or"biology":
    subjects.remove(whichdelete)
    print(subjects)

#q3
colours = ["blue","green","red","purple","pink","yellow","white","orange","black","grey"]
print(colours)
number1 = int(input("which is your first number between 1 and 4: "))
number2 = int(input("which is your second number between 5 and 9: "))
if number1 > 4:
    print("retry number 1")
else:
    print("number1 is valid")
if (number2 < 5) or (number2 > 9):
    print("retry number 2")

else:
    print("number2 is valid")

print(colours[number1:number2])

#q4
listofnum = [123, 456, 789]
print(listofnum[0])
print(listofnum[1])
print(listofnum[2])
usernums = int(input("please enter your 3 digit number: "))
if listofnum[0] == usernums: # listofnum[2] == usernums:
    print(listofnum[0],"is the first number in the list")
elif listofnum[1] == usernums:
    print(listofnum[1],"is the second number in the list")
elif listofnum[2] == usernums:
    print(listofnum[2],"is the last number in the list")
else:
    print("this is not in the list")

#q5
partylist = []
name = 0
digit = 0
a = 0
while name != 3:
    invite = input("please enter a name: ")
    partylist.insert(digit,invite)
    name = name + 1
    invite = ""
    digit = digit + 1
if name == 3:
    retry = input("do you want to add another name: ")
    
if retry == "no":
    print(partylist)
    
if retry == "yes":
    while a != 1:
        invite = input("please enter a name: ")
        partylist.insert(digit,invite)
        invite = ""
        digit = digit + 1
        retry1 = input("do you want to add another name: ")
        if retry1 == "no":
            a = a + 1
            print(partylist)
print("there are",len(partylist),"people coming to the party")

#q6
partylist1 = [] 
name1 = 0
digit1 = 0 
a1 = 0 
while name1 != 3:
    invite1 = input("please enter a name: ") 
    partylist1.insert(digit1,invite1)
    name1 = name1 + 1
    invite1 = ""
    digit1 = digit1 + 1
if name1 == 3:
    retry1 = input("do you want to add another name: ")
    
if retry1 == "no":
    print(partylist1)
    
if retry1 == "yes":
    while a1 != 1:
        invite1 = input("please enter a name: ")
        partylist1.insert(digit1,invite1)
        invite1 = ""
        digit1 = digit1 + 1
        retry1 = input("do you want to add another name: ")
        if retry1 == "no":
            a1 = a1 + 1
            print(partylist1)
print("there are",len(partylist1),"people coming to the party")

whichguest = input("please enter a name thats on the list: ")
print(whichguest,"is in position",(partylist1.index(whichguest) + 1),"on the list")
delguest = input("do you want this guest to come: ")
if delguest == "yes":
    print(partylist1)
elif delguest == "no":
    p = partylist1.index(whichguest)
    del partylist1[p]
    print(partylist1)
 
#q7
line = 0
shows = ["friends","steinfeld","archer","south park"]
amountofshows = len(shows)
while line != amountofshows:
    print(shows[line])
    line = line + 1

usershow = input("please enter a name of a new show thats not on the list: ")
userposition = int(input("where would you like this show positioned: "))
shows.insert((userposition - 1),usershow)
print(shows)

#q8
nums = []
numlength = len(nums)
lastnumber = -1
while numlength != 3:
    usernum1 = int(input("what number would you like to enter: "))
    nums.append(usernum1)
    numlength = len(nums)
    lastnumber = lastnumber + 1
keepnum = input("do you want the last number you entered: ")
if keepnum == "yes":
    print(nums)
elif keepnum == "no":
    del nums[lastnumber]
    print(nums)
    
    

