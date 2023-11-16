#strings and functions
#q1
name = input("what is your name: ")
print(len(name))

#q2
fname =  input("what is first name: ")
lname =  input("what is last name: ")
bothlen = (len(fname) + len(fname)) 
print(fname, lname, "the length is",bothlen)
#

#q3
fnamelower =  input("what is first name in lower case: ")
lnamelower =  input("what is last name in lower case: ")
fnamelower = fnamelower.upper()
lnamelower = lnamelower.upper()
print(fnamelower, lnamelower)

#q4
rhyme = input("start of a nursery rhyme:") # mary had a little lamb
print("there are characters:", (len(rhyme)))
stnumber = int(input("start number"))
ednumber = int(input("end number"))
print(rhyme[stnumber:ednumber])

#q5
anyword =  input("type any word in lower case: ")
anyword = anyword.upper()
print(anyword)

#q6
fname1 = input("what is your first name: ")
if len(fname1) < 5:
    lname1 =  input("what is last name: ")
    bothname = fname1 + lname1
    bothname = bothname.upper()
    print(bothname)
elif len(fname1) >= 5:
    fname1 = fname1.lower()
    print(fname1)

#Q7
userword1 = input("what is your word: ")
x = userword1[0]
if userword1[0] in ["a", "e", "i", "o", "u"]:
    userword1 = userword1 + "way"
    userword1 = userword1.lower()
    print(userword1)
else:
    userword1 = userword1.replace(x,"")
    userword1 = userword1 + x
    userword1 = userword1 + "way"
    print(userword1)
    