

#for loops = execute a block of code a fixed number
#of times

#using range function
#for x in range(1, 11):
#    print(x)

#you can use steps in range function

#for x in range(1, 10, 2) :
#    print(x)

#we can use reversed function for revers itration 

for x in reversed(range(1, 11, 2)): 
    print(x)

#we can use to iterate through string 

credit_card = "123-230-254-586"

for i in credit_card:
    print(i)