#Q1
"""
a = input("whats ur name: ")
length1 = len(a)
print("the lenght of ur name is",length1,"letters")

#Q2
b = input("whats ur first name: ")
c = input("whats ur surname: ")
print ("your name is",b,c)
d = len(b) + len(c)
print("the lenght of ur full name is",d,"letters")

#Q3
e = input("whats ur first name (in lower case): ")
f = input("whats ur surname (in lower case): ")
E = e.upper()
F = f.upper()
print ("your name is",E,F)

#Q4
g = input("first line of a nusery rhyme") # humpty dumpty sat on the wall
h = len(g)
i = int(input("starting number"))
j = int(input("ending number"))
k = g[i:j]
print(h)
print(k)

#Q5
l = input("type any word: ")
L = l.upper()
print ("your word is",L)

#Q6
m = input("whats ur first name: ")
if (len(m) >= 5):
    m = m.lower()
    print("ur name is:",m)
    
elif (len(m) < 5):
    n = input("whats ur surname: ")
    o = m + n
    o = o.upper()
    print("ur name is:",o)
"""

#Q7
p = str(input("type any word: ")) #pig aarvark
q = p[0]
print(q)
if (q == "a","e","i","o","u","A","E","I","O","U"):
    r = p + "way"
    R = r.lower()
    print(R)
elif (q != "a","e","i","o","u","A","E","I","O","U"):
    s = 