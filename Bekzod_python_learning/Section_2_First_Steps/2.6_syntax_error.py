#A SyntaxError in Python occurs when your code violates the language's grammatical rules, 
#preventing the program from running. The interpreter detects this error during the initial parsing phase and 
#will provide a message indicating the file, line number, and a caret (^) pointing to where the issue was first detected, 
#which is often helpful but can sometimes be misleading. 


# ______________________ Arithmetic operations _______________________
print(2+4*2) # 10

"""Key Rules
Parentheses override all other rules: Any expression inside parentheses () is evaluated first, regardless of the operators involved.
Multiplication and Division have the same precedence: When an expression contains both, they are evaluated from left to right.
Example: 100 / 10 * 10 is evaluated as (100 / 10) * 10 which equals 10.0 * 10 = 100.0.
Addition and Subtraction have the same precedence: They are also evaluated from left to right.
Example: 5 - 2 + 3 is evaluated as (5 - 2) + 3 which equals 3 + 3 = 6.
Exponentiation is right-associative: 2 ** 3 ** 2 is evaluated as 2 ** (3 ** 2), which calculates 3 ** 2 (9) first, then 2 ** 9 (512).  """

print(19/5) # 3.8
print(20/5) # 4.0 
print(10//3) # 3
print(9//3) # 3
print(2**4) # 16

# We can combine string and numbers within print(). After every string and number use (,)
print("To'qqizning kvadrati", 9**2, "ga teng")


