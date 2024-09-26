'''
Name: Duncan Staats
Date: 9-16-2024
Description: Unit 2 Lesson 1 Notes

'''


#Variables - store information

message = "Hello, user" #string variable
print(message)

#snake_caes to name our variable
user_name = input("Enter your name:  ")
user_id = int(input("Enter your id:  "))

# variable type command
#print(type(user_name))

# Type 1 -strings
# can use ' or " to indicate string - be consistent

# f strings are formatted strings that help with combing strings
# way 1 to combin strings: use + (concatenation)
#caution: all numbers have to have str() around them
message_one = "welcome " + user_name + " with ID " + str(user_id)
print(message_one)

#way 2 - use f strings
message_two = f"welcome {user_name} with ID {user_id}"
print(message_two)

#possiable errors
#apostrophes inside of single quotes
#resolution: use escape sequence \ - tells python next symbol is literally that thing, no pythonic meaning
famous_quotation = 'Keep your friends close and your opponent\'s - closer'

#raw strings
hippo = r"""


             ..ed$$$$$$$$$$$$$be      *F..
       ^   z$$$$$$$$$$$$$$$$$$$$$$$$$$$$
          $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$.
         $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$*e.
        4$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$be$$$$$$c
        4$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$L
        ^$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
         ^*$$$$$$$$$$$$$$$$$$$$$$$$$$$F^*$$$$$$$$$%
           ^"$$$$$$$$$$$$$$$$$$$$$$$$$    
             4$$$F"3$$$$       4$$$$
             d$$$$ 4$$$$       4$$$$                 Hippo
                                                     ^^^^^"""
print(hippo)