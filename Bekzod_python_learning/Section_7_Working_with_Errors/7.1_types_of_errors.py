# A Python syntax error occurs when your code violates the grammatical rules of the Python language, 
# preventing the interpreter from running the program. 
# These errors are usually caught during the initial parsing stage, 
# and Python will point you to the line where it detected the issue. 

#print "Hello World!"  # SyntaxError: Missing parentheses in call to 'print'. Did you mean print('Hello World!')

# EOL - End of Line
# print("Hello World! # SyntaxError: unterminated string literal (detected at line 9)

# EOF - End of function:
# print("Hello World!"  # SyntaxError: '(' was never closed


# IndentationError:
#  print("Hello World!") # IndentationError; unexpected indent


# print("Count to ten")
# for n  in range(10):
# print(n+1) # IndentationError: expected an indented block

# son = 50
# if son>=0:
#     print('Musbat son')
# else:
# print("Manfiy son") # IndentationError: expected an indented block after 'else' statement on line 26




#  RUN TIME ERROR:
# A runtime error in Python occurs when the program, 
# although syntactically correct, encounters an unforeseen problem 
# during execution that causes it to halt unexpectedly. 
# These errors are also known as exceptions and are distinct from syntax errors,
# which prevent the program from running at all. 

# 1) TypeError:
# son = input("Istalgan son kiriting: ")
# print(f"{son}ning kvadrati {son**2} ga teng.") # TyperError: unsupported operand type(s) for ** or pow(): 'str' and 'int'

# 2) NameError:
# prit("Hello Wordl!") # NameError: name 'prit' is not defined. Did you mean 'print'?

# mevalar = ['olma', 'uzum', 'nok', 'anor', 'anjir']
# for meva in mvelar:
#     print(meva) # NameError: name 'mvealar' is not defined


# 3) ValueError:
# son = int(input("Istalgan son kiriting: "))
# if son>=0:
#     print("Musbat son")
# else:
#     print('Manfiy son')
# If we enter the value of 5.5(for example), it will be ValueError: invalid literal for int() with base 10: '5.5'


# 4) IndexError:
# mevalar = ['olma', 'anor', 'uzum']
# print(mevalar[3]) # IndexError: list index out of range


# 5) ZeroDivisionError:
# x, y = 50, 50
# z = 250/(x-y) # x-y = 0


# Logical Errors:
# radius = 5
# pi = 4.14 # The real pi = 3.14
# aylana_yuzi = pi*radius**2
# print(aylana_yuzi)
# Result: 103.499999999999999


# son = float(input("Istalgan son kiriting: "))
# ildiz = son**1/2 
# print(f"{son} ning ildizi {ildiz} ga teng.")
# Logical Error: it should be  "ildiz = son**(1/2)"

# mevalar = ['olma', 'uzum', 'nok', 'anor', 'anjir']
# for meva in mevalar:
#     print(meva)
#     print("Dastur tugadi.")


# Practice:
# 1)
# son = float(input("Juft son kiriting: "))
# if not son%2==0:
#     print("Bu son juft son emas.")
# else:
#     print("Rahmat!")

# 2)
# yosh = int((input("Yoshingiz nechida? ")))
# if yosh <=4 or yosh>=60:
#     narx = 0
# elif yosh<18:
#     narx = 10000
# else:
#     narx = 20000
# print(f"Chipta narxi {narx} so'm")

# 3)
# x = int(input("Birinchi sonni kiriting: "))
# y = int(input("Ikkinchi sonni kiriting: "))
# if x == y:
#     print(f"{x}={y}")
# elif x<y:
#     print(f'{x}<{y}')
# else:
#     print(f'{x}>{y}')


# 4)
# mahsulotlar = ['un', 'yog', 'sovun', 'tuxum', 'piyoz', 'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
# savat = []

# for n in range(5):
#     savat.append(input(f"{n+1} - mahsulotni qo'shing: ").lower())

# if savat:
#     for mahsulot in savat:
#         if mahsulot in mahsulotlar:
#             print(f"Do'konimizda {mahsulot} bor")
#         else:
#             print(f"Do'konimizda {mahsulot} yo'q")
# else:
#     print("Savatingiz bo'sh")


# 5)
# users = ['alisher1983', 'aziza', 'yasina', 'umar']

# login = input("Yangi login tanlang: ")
# if login in users:
#     print('Login band, yangi login tanlang!')
# else:
#     print("Xush kelibsiz")

