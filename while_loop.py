#while loops = execute some code WHILE some condition 
#remains true 
"""
name = input("Enter your name: ") 

while name == "" :
    print("you did not enter your name")
    name = input("Enter your name: ")

else:
#f is used to get the name in string format 
# it is f-string 
    print(f"your name is: {name}" )
"""
"""
# another example in while loop 

food = input("Enter the food you like (q to quit): ")
# not logical operator 
while not food == "q" :
    print(f"you like {food}")
    food = input("Enter another food (q to quit): ")

print("bye")

"""

#another example and usage of or logical operator 

num = int(input("Enter a number between (1-10) : "))

while num < 0 or num > 10 :
    print(f"{num} is not valid")
    num = int(input("Enter a number between (1-10): "))

print("your number is {num}")