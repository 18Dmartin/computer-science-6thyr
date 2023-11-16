"""
1.
a = D, b = E, c = F, d = G, e = H, f = I, g = J, h = K, i = L, j = M, k = N, l= O, m = P, n = Q, o = R, p = S, q = T, r = U, s = V, t = W, u = X, v = Y, w = Z, x = A, y = B, z = C,

2.
WKRPDV = Thomas

4.
ZKDW = what
GR = do
BRX = you
JHW = get
ZKHQ = when
BRX = you
FURVV = cross
D = a
VQRZPDQ = snowman
ZLWK = with
D = a
YDPSLUH? vampire
IURVWELWH = frostbite

5.
"""
usermessage = str(input("enter a message: ")) #what = ZKDW
encodeordecode = str(input("do you want the message encoded or decoded: "))
keynum = str(input("what do you want the key number to be: "))
print(usermessage, "Is your message");
print(keynum, "Is your number");
if encodeordecode == 'encoded':
    print("encoded")
if encodeordecode == "decoded":
    print("decoded")

usermessagelength = len(usermessage)
#decoded
if encodeordecode == "decoded":
    ALPHA = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N","O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    #break user code into code

userarray = usermessage.split(" ")
print(userarray)

