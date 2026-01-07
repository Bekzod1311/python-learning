# yosh = input("Yoshingizni kiriting: ")
# try:
#     yosh = int(yosh) # xato qaytaradigan kod
#     print(f"Siz {2026-yosh} yilda tug'ilgansiz")
# except: # xato yuz bergan bajaruvchi  kod
#     print("Butun son kiritmadingiz")


# while True:
#     yosh = input("Yoshingizni kiriting: ")
#     if yosh.isdigit():
#         yosh = int(yosh)
#         break
# print(f"Siz {2026-yosh} yilda tug'ilgansiz")


#  Practice:
# 1)
# x = int(input("son kiriting: "))
# y = int(input("yana bir son kiriting: "))
# print(x, '/', y, '=', x/y)

# x = int(input("son kiriting: "))
# y = int(input("yana bir son kiriting: "))
# try:
#     x = int(x)
#     y != 0
#     print(x, '/', y, '=', x/y)
# except ZeroDivisionError:
#     print("Sonni 0 ga bo'lib bo'lmaydi.")


# while True:
#     x = input("Birinchi son: ")
#     y = input("Ikkinchi son: ")
#     if  int(y) != 0:
#         x = int(x)
#         y = int(y)
#         print(x, '/', y, '=', x/y)
#     else: 
#         print("Butun son kiriting va bo'luvchi son 0 ga teng bo'lmasin.")