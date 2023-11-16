things = "mystuff"
a1 = things[1]
a2 = things[-1]
a3 = things[1:5]
a4 = things.upper()
a5 = things.lower()
a6 = things.count("f")
a7 = things.find("s")
a8 = things.replace("s","z")
a9 = things.islower()
a10 = things.isupper()
a11 = things.isalnum()
a12 = things.isalpha()
a13 = things.isdigit()
a14 = things.index("s")
a15 = things.strip("f")
print(a1, a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15)

ooga = ["booga","looga",34,546]
b1 = ooga[0] = "mooga"
b2 = ooga[2]
b3 = ooga[-2]
b4 = ooga[0:3]
b5 = ooga[0:]
del ooga[3]
b6 = ooga.append("mooga")
b7 = ooga.extend("mooga")
b8 = ooga.insert(5,"wooga")
ooga.remove("looga")
b10 = ooga.pop(2)
b11 = ooga.index("wooga")
b12 = ooga.count("546")
b13 = ooga.reverse()
b14 = ooga.copy()
print(b1, b2,b3,b4,b5,b6,b7,b8,b10,b11,b12,b13,b14)
b = ooga.clear()