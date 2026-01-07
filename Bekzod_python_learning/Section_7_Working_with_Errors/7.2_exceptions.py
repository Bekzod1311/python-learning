# try-except:

# yosh = input("Yoshingizni kiriting: ")
# yosh = int(yosh)
# print(f"Siz {2025-yosh} yilda tug'ilgansiz.")

# yosh = input("Yoshingizni kiriting: ")
# try:
#     yosh = int(yosh) # xato qaytargan qator
#     print(f"Siz {2025-yosh} yilda to'g'ilgansiz.")
# except: # xato yuz bergan bajaruvchi kod
#     print("Butun son kiritmadingiz")
# print("Dastur tugadi.")


# try-except-else:
# yosh = input("Yoshingizni kiriting: ")
# try:
#     yosh = int(yosh)
# except:
#     print('Butun son kiritmadingiz.')
# else:
#     print(f"Siz {2025-yosh} yilda tug'ilgansiz.")



# yosh = input("Yoshingizni kiriting: ")
# try:
#     yosh = int(yosh)
# except ValueError:
#     print('Butun son kiritmadingiz.')
# else:
#     print(f"Siz {2025-yosh} yilda tu'gilgansiz.")


# x, y = 5 , 10
# try:
#     y/(x-5)
# except ZeroDivisionError:
#     print("0 ga bo'lib bo'lmaydi.")

# mevalar = ['olma', 'anor', 'anjir', 'uzum']
# try:
#     print(mevalar[7])
# except IndexError:
#     print(f"Ro'yxatda {len(mevalar)} ta meva bor xolos")


# Key Error
# user = {
#     "username":'sariqdev',
#     "status":'admin',
#     "email":'admin@sariq.dev',
#     "phone":'99897123456',
# }
# key = "tel"
# try:
#     print(f"Foydalanuvchi: {user[key]}")
# except KeyError:
#     print("Bunday kalit mavjud emas.")


# FileNotFoundError:
# fayl = 'data.txt'
# try:
#     f = open(fayl)
# except FileNotFoundError:
#     print(f"{fayl} fayli mavjud emas.")


# n = input('Butun son kiriting: ')
# try:
#     n = int(n)
#     x = 20/n
# except ValueError:
#     print("Butun son kiriting") # agar foydalanuvchi butun son kiritmasa.
# except ZeroDivisionError: # agar foydalanuvchi 0 kiritsa,
#     print("0 ga bo'lib bo'lmaydi")
# else:
#     print(f"x = {x}")


user = {'username':'sariqdev',
        "status":'admin',
        "email":'admin@sariq.dev',
        "phone":'99897123456'}
key = "tel"
try:
    print