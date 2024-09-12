#nested loop = loop within another loop (outer, inner)

#   outer loop 
#        inner loop


#example print 1-9 three times 
"""
for x in range(3) :
    for y in range(1, 10) :
        print(y, end = "")
    print("")
"""

#print a rectangle

rows = int(input("print number of rows: "))
columns = int(input("Enter # of columns: ")) 
symbol = input("Enter the symbol: ")

for x in range(rows) : 
    for y in range(columns):
        print(f"{symbol}", end= "")
    print("")