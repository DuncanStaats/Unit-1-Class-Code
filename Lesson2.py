'''
Name: Duncan Staats
Date: September 24, 2024
Description: More on F-strings, input and numbers/ops
'''
print("My first commit.")

my_int = 5
my_float = 6.38
print(f"{my_int} {my_float}")

another_float = 8 #make this a float by adding .0
float_two = float(8) # make a float by casting
print(f"{another_float} {float_two}")

#get decimal from a user
radius = float(input("Enter a radius: "))
print(f"You entered a radius of {radius}")

# operations on numbers
#P E MModD AS
# modulus operator or remainder operator
print(15 % 7) #Prints the remainder when 15 is divided by 7
print((2+3)*4)

# exponent is not ^, it is **
print(5**4) #this is 5^4
print(5^3) #this is not right
#werid math stuff
print(0.3-0.2)

#rounding
#method 1, use round()
num = 3.1415
print(round(num,2))
#method 2, use f-string
print(f"{num:.2f}")

#your turn to code
#ask a user for some amount of US dollars'
# store this in a variable
#convert that money to some currency of your choice
#store the conversion factor in a variable
#store the final amount in a variable
#Print it like "___ USD is the same as ___ CAD".
#round to 2 decimal places

num_1 = float(input("How many US dollars do you want to convert: "))
num_2 = float(num_1*42105) #Iranian Rail
num_3 = float(round(num_2,2))

print(f"{num_1} USD is the same as {num_3} IRR")

# string methods
name = "lee cat"
name2 = "BOB BUILDER"
print(name2.lower())
print(name.upper())
print(name.title())