#q1 and q2 
whichQ = input("a or b or c or d or e: ")
if whichQ =="a":
    sentence = input("Enter a sentence: ")
    chars = {}
    for char in sentence:
        if char in chars:
            chars[char] = chars[char] + 1
        else:
            chars[char] = 1
    print(chars)
#this program breaks the sentence up into individual characters
#and find how many times a single letter has been used

elif whichQ =="b":
    sentence = input("Enter a sentence: ")
    chars = {}
    for char in sentence:
        print(char)
        if char in chars:
            chars[char] = chars[char] + 1
    
#this breaks the sentence up and prints evry character on an individual lines

#chars == to a dictionary
            
#chars hold letters
#values hold the amount of time it is used

elif whichQ =="c":
    sentence = input("Enter a sentence: ")
    chars = {}
    for char in sentence:
        chars[char] = chars.get(char, 0) + 1
    print(chars)
#it allows the code to work as initially intended

#Return the value for key if key is in the dictionary, else default.
#If default is not given, it defaults to None, so that this method
#never raises a KeyError.
    
elif whichQ =="d":
    sentence = input("Enter a sentence: ")
    chars = {}
    vowels = "aeiou"
    for char in sentence:
        if char in vowels:
            
                chars[char] = 1
    print(chars)
    
    
elif whichQ =="e":
    sentence = input("Enter a sentence: ")
    vowels = "aeiou" 
    chars = {"vowels" : 0 , "consonants" : 0}
    for char in sentence:
        if char in vowels:
            chars["vowels"] = chars["vowels"] + 1
        else:
            chars["consonants"] = chars["consonants"] + 1
    print(chars)
    
elif whichQ =="f":
    sentence = input("Enter a sentence: ")
    chars = {}
    for char in sentence:
        print(char)
        if char in chars:
            chars[char] = chars[char] + 1

    
