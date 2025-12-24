# In Python, the if statement is a fundamental control flow statement used for decision-making, 
# allowing the program to execute specific blocks of code only if a given condition is met. 

# Basic if Statement
# A basic if statement evaluates a condition that results in either True or False. 
# If the condition is True, the indented code block (called a "suite") is executed; otherwise, it is skipped. 

# son = int(input("'Istalgan son kiriting: "))
# if son>0:
#     print(son, 'musbat son')

# yosh = int(input("Yoshingizni kiriting: "))
# if yosh <= 7:
#     print("Sizga avtobus tekin")
# else:
#     print("Chipta narxi 5000 so'm")


# yosh = int(input('Yoshingiz nechida? '))
# if yosh>65: print("Siz COVID-19 risk guruhidasiz")

# x, y = 25, 50
# print("x>y") if x > y else print("x<y")

# ism = 'Ali'
# ism.lower() == 'ali'



# Practice: 
# avtolar = ['audi', 'bmw', 'volvo', 'kia', 'hyundai']
# for avto in avtolar:
#     if avto == 'bmw':
#         print(avto.upper())
#     else:
#         print(avto.title())

# javob = float(input("12x6 nechiga teng? "))
# if javob != 72:
#     print("Javob xato")

# yosh = int(input("Yoshingiz nechida? "))
# if yosh >= 18:
#     print("Xush kelibsiz")
# else:
#     print("Kirish mumkin emas")

# yil = int(input("Tug'ilgan yilingizni kiriting: "))
# if 2025-yil<18:
#     print(f"Yoshingiz {2025-yil} da ekan.")
#     print("Kirish mumkin emas.")
# else:
#     print("Xush kelibsiz.")

# login = input("Yangi login kiriting: ")
# if len(login) <= 5:
#     print("Login 5 harfdan ko'proq bo'lishi shart!")


# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
    # if car == "gm":
    #     print(car.upper())
    # else:
    #     print(car.title())

    # if car != 'gm':
    #     print(car.title())
    # else:
    #     print(car.upper())

# admin = 'Bekzod Khusanov'
# login = input("Login nomizni kiriting: ")
# if login.title() == admin:
#     print("Xush kelibsiz, Admin.")
#     print("Foydalanuvchilar ro'yxatini ko'rasizmi? ")
# else:
#     print(f"Xush kelibsiz {login.title()}")


# son1 = int(input("Birinchi sonni kiriting: "))
# son2 = int(input("Ikkinchi sonni kiriting: "))
# if son1 == son2:
#     print("Sonlar teng.")
# else:
#     print("Sonlar teng emas.")


# son1 = int(input("Istalgan son kiriting: "))
# if son1 > 0:
#     print("Bu musbat son.")
# else:
#     print("Bu son manfiy.")

# son1 = int(input("Musbat son kiriting: "))
# if son1 > 0:
#     print(f"Sonning ildizi {son1**(1/2)}")
# else:
#     print("Musbat son kiriting.")

# son1 = int(input("Son kiriting: "))
# if son1 % 2 == 0:
#     print("Bu son juft son.")
# else:
#     print("Bu toq son.")