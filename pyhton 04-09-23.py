# initialise the variable
runningTotal =0 

# preform the calculations
Price1 = 10 
runningTotal = runningTotal + Price1
Price2 = 24
runningTotal = runningTotal + Price2
Price3 = 6
runningTotal = runningTotal + Price3

#display the output
print("the running total is ",runningTotal)


fin = open("assignment 2.py")
print(fin)
for line in fin:
    print(line.strip())
    fin.close()