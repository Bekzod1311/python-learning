#______________________COMMENTS_________________________#
# In Python, comments are non-executable notes in the source code that are ignored by the interpreter during program execution. They are used to make code more readable, explain logic, and help with documentation or debugging. 
# Types of Comments
# 1. Single-Line Comments
# The primary way to create a comment in Python is by using the hash symbol (#). Any text following the # on the same line is considered a comment. 

# This is a single-line comment in Python
# print("Hello, World!") # An inline comment after a statement

# 2. Multi-Line Comments (Block Comments)
# Multiple # symbols: The standard and most "Pythonic" way for a block comment is to place a # at the beginning of each line.
# This is a multi-line comment
# created by using multiple
# single-line comments.

#Triple-quoted strings: You can use triple quotes (""" or ''') to enclose a block of text. 
#If this string is not assigned to a variable, the interpreter ignores it, effectively treating it as a comment.

"""
This is also used for multi-line comments,
though technically it's a string literal
that isn't assigned to a variable.
"""


#print(2*5*3.14159)  # NO.1

# Radiusi 5 ga teng bo'lgan aylananing uzunligi: NO.2
#print(2*5*3.14159)

# print("Assalomu alaykum!") # ushbu qator bajariladi
# Keyingi qator esa bajarilmaydi
# print("Mening ismim Bekzod")



#Practice
print("\"Nexia\", \"Tico\", 'Damas' ko'rganlar qilar havas")

# 5 ning 4-darajasini toping
print(5**4)
# 22 ni 4 ga bo'lganda qancha qoldiq qoladai?
print(22%4)
# Tomonlari 125 ga teng kvadratning yuzi va perimetrini toping.
print("Perimetr teng ", 125*4, "ga")
print("Yuza teng ", 125*125, "ga")
# Diametri 12ga teng bo'lgan doiraning yuzini toping
pi = 3.14
d = 12
r = d/2
print(pi*r**2)
# Katetlari 6 va 7 bo'lgan to'g'ri burchakli uchburchaknining gipotenuzasini toping (Pifagor teoremasidan foydalaning)
print("Gipotenuza teng ", (6**2+7**2)**0.5, "ga teng")