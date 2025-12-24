# In Python, variables are symbolic names that act as labels or references to objects stored in memory, 
# used to store and manage data during program execution. Unlike some other languages, 
# you don't need an explicit declaration command; a variable is created 
# the moment you assign a value to it using the assignment operator (=). 

# ism = "Abdulloh"
# yosh = 25
# print(ism)    # Abdulloh
# print(yosh)   # 25

#  You can change the value of the variable at any time
# ism = "Abdulloh"
# print(ism)
# ism = "Murod"
# print(ism)



# In Python, variable naming is governed by specific rules and conventions to ensure code is valid and readable. 
# Mandatory Rules
# Failing to follow these rules will result in a SyntaxError: 
# Allowed Characters: Variable names can only contain letters (A-z), numbers (0-9), and underscores (_).
# Must Start with Letter or Underscore: A variable name must begin with a letter or an underscore, never a number. (e.g., _age or name, but not 2items).
# No Python Keywords: You cannot use any of Python's reserved keywords (like if, for, class, None, True, False, etc.) as a variable name.
# No Spaces or Special Characters: Spaces and special symbols (e.g., !, @, #, $, %, -) are not allowed.
# Case-Sensitive: Variable names are case-sensitive, meaning age, Age, and AGE are all different, distinct variables. 

# Recommended Conventions (PEP 8)
# While not mandatory rules, these conventions, outlined in the PEP 8 style guide, are widely followed by Python programmers for writing clean, readable code: 
# Use snake_case: For standard variable and function names, use lowercase letters and separate multiple words with underscores (e.g., first_name, total_volume).
# Be Descriptive: Choose names that clearly describe the variable's purpose. active_user is better than au.
# Avoid Ambiguous Letters: Do not use the lowercase letter l, the uppercase letter O, or the uppercase letter I, as they can be easily confused with the numbers 1 and 0.
# "Constants" Use ALL_CAPS: Although Python doesn't have true constants, variables intended not to be changed throughout the program are conventionally written in all capital letters with underscores (e.g., FILE_SIZE_LIMIT).


# PRACTICE
word = "Hello World!"
print(word)

xabar = "Here you can put your advertisement"
print(xabar)
xabar = "We are re-opening under new management"
print(xabar)

# class = "It won't work as it is keyword"
# print(class)

radius = 5
pi = 3.14159
yuza = pi * radius**2
print("Radius", radius,"ga teng doira yuzi=", yuza)