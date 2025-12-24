# The while loop in Python is a control flow statement that repeatedly 
# executes a block of code as long as a given condition remains True. 
# It is typically used when the number of iterations required is not known in advance. 

# Key Components
# Condition: An expression that evaluates to either True or False. 
# The loop continues as long as this expression is True.
# Indentation: Python uses indentation to define the scope of the loop body. 
# All indented statements are part of the loop.
# Loop Control Statements:
# break: Immediately terminates the loop entirely, regardless of the condition's status.
# continue: Skips the current iteration and jumps back to the loop's condition check.
# else clause: An optional block that executes only if the loop terminates normally (i.e., the condition becomes False), 
# and not because of a break statement. 

# son = 1
# while son <=5: # toki son 5 dan kichik yoki teng ekan...
#     print(son, end = ' ')
#     aon += 1


# while and input():
# print('Kiritilgan sonning kvadratini qaytaruvchi dastur.')
# savol = 'Istalgan son kiriting '
# savol += "(to'xtatish uchun 'exit' deb yozing): "
# qiymat = ' '
# while qiymat != 'exit':
#     qiymat = input(savol).lower()
#     if qiymat != 'exit':
#         print(float(qiymat)**2)

# print("Kiritilgan sonning kvadratini qaytaruvchi dastur: ")
# savol = "Istalgan son kiriting "
# savol += "(to'xtatish uchun 'exit' ni kiriting.): "
# ishora = True
# while ishora:
#     qiymat = input(savol).lower()
#     if qiymat == 'exit':
#         ishora = False
#     else:
#         print(float(qiymat)**2)

# print("Kiritilgan sonning kvadratini qaytaruvchi dastur ")
# savol = "Istalgan son kiriting "
# savol += "(to'xtatish uchun 'exit' deb yozing. ): "
# while True: # abadiy sikl
#     qiymat  = input(savol)
#     if qiymat == 'exit':
#         break  # siklni to'xtat
#     else:
#         print(float(qiymat)**2)

# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5:
#         break
#     print(f"{son} ning kvadrati {son**2} ga teng.")

# sonlar = list(range(1,11))
# for son in sonlar:
#     if son ==5:
#         continue
#     print(f"{son} ning kvadrati {son**2} ga teng.")


# son = 0
# while son < 10:
#     son += 1
#     if son%2 != 0:
#         continue
#     else:
#         print(son, end = ' ')
    
# Infinity loop
# son  = 0
# while son < 10:
#     if son % 2 != 0:
#         continue
#     else:
#         print(son)

# son = 0
# while son < 10:
#     if son%2 != 0:
#         continue
#     else:
#         print(son)
#     son += 1


# Practice:
# 1)
# print("Kitob nomlarni qaytaruvchi dastur")
# gap = 'Istalgan kitob nomini kiriting '
# gap += "(dasturni to'xtatish uchun 'stop' deb yozing): "
# savol = " "
# while savol != 'stop':
#     savol = (input(gap))
#     if savol == 'stop':
#         break
#     else:
#         print(savol)

# 2)
# print('Muzeyga xush kelibsiz: ')
# gap = "\nYoshingizni kiritng va chipta narxini bilib oling. \n"
# gap += "(dasturni to'xtatish uchun 'exit' yoki 'quit' deb yozing.): "
# yosh = " "
# while yosh != 'exit' and yosh != 'quit':
#     yosh = input(gap).lower()
#     if yosh == 'exit' or yosh == 'quit':
#         break
#     elif int(yosh) < 7:
#         print('Chipta narxi: 2000 so\'m.')
#     elif int(yosh) < 18:
#         print("Chipta narxi: 3000 so'm.")
#     elif int(yosh) < 65:
#         print("Chipta narxi: 10000 so'm.")
    
#     else:
#         print("Sizga kirish bepul.")

# 3) 
# savol = "Kiritilgan sonning idizini qaytaruvchi dastur. \n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input(savol)
#     if qiymat.title() == 'Exit':
#         break
#     elif float(qiymat) < 0:
#         continue
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng.")    
