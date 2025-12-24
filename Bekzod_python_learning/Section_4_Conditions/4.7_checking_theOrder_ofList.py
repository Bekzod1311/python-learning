# 'in' operation

# menu = ['osh', 'qozonkabob', 'shashlii', 'norin', 'somsa']
# print('manti' in menu) # is there "manti" in menu? # False.
# print('osh' in menu) # is there "osh" in menu? # True.

# menu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa']
# ovqat = input("Nima ovqat yeysiz? ")
# if ovqat.lower() in menu:
#     print("Buyurtma qabul qilindi.")
# else:
#     print("Afsuski bizda bunday ovqat yo'q")


# menyu = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa']
# print('manti' not in menyu) #  menyu da manti yo'qmi?  # True
# print('osh' not in menyu) # False


# menyu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa']
# ovqat = input('Nima ovqat yeysiz? ')
# if ovqat.lower() not in menyu:
#     print("Afsuski, bizda bunday ovqat yo'q")
# else:
#     print('Buyurtma qabul qilindi.')


# menyu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa']
# buyurtmalar = ['osh', 'somsa', 'manti', 'shashlik']
 
# for taom in buyurtmalar:
#     if taom in menyu:
#         print(f"Menyuda {taom} bor")
#     else:
#         print(f"Kechirasiz, menyuda {taom} yo'q.")



# list1 = [1, 2, 3]
# print(len(list1) > 0) # True

# list2 = []
# print(len(list2)>0) # False

# list1 = [1, 2, 3]
# if list1: # Bu ifoda True qaytaradi, sababli, list1 bo'sh emas.
#     print("Ro'yxatda elementlar bor")


# menyu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa']
# buyurtmalar = ['osh', 'somsa', 'manti', 'shashlik']

# if buyurtmalar:
#     for taom in buyurtmalar:
#         if taom in menyu:
#             print(f"Menyuda {taom} bor")
#         else:
#             print(f"Kechirasiz, menyuda {taom} yo'q")
# else:
#     print("Savatchangiz bo'sh")



# Practice
# son = int(input("Juft son kiritin: "))
# if son%2 == 0:
#     status = "Rahmat"
# else:
#     status = "Juft son kiriting"
# print(status)


# age = int(input("Yoshingizni kiriting: "))
# if age > 60 or age < 4:
#     price = 'bepul'
# elif age < 18:
#     price = "10000 so'm"
# else:
#     price = "20000 so'm"
# print(f"Sizga muzeyga kirish {price}")

# son1 = int(input("Birinchi sonni kiriting: "))
# son2 = int(input("Ikkinchi sonni kiriting: "))
# if son1>son2:
#     print("Birinchi son katta.")
# elif son1<son2:
#     print("Ikkinchi son katta")
# else:
#     print("Sonlar teng!")


# mahsulotlar = ['tuz', 'tuxum', 'sut', 'guruch', "go'sht", 'un', 'olma', 'sabzi', 'pishloq', 'shakar']
# savat = []
# for n in range(1,6):
#     savat.append(input(f"{n} - mahsulotni kiriting: "))
# print(savat)
# for m in savat:
#     if m.lower() in mahsulotlar:
#         print(f"{m} mahsuloti do'konimizda bor.")
#     else:
#         print(f"{m} mahsuloti do'konimizda yo'q.")



# mahsulotlar = ['tuz', 'tuxum', 'sut', 'guruch', "go'sht", 'un', 'olma', 'sabzi', 'pishloq', 'shakar']
# savat = []
# bor_mahsulotlar = []
# mavjud_emas = []
# for n in range(1,6):
#     savat.append(input(f"{n} - mahsulotni kiriting: "))
# print(savat)
# for m in savat:
#     if m.lower() in mahsulotlar:
#         bor_mahsulotlar.append(m)
#     else:
#         mavjud_emas.append(m)
# if len(mavjud_emas) <= 0:
#     print("Siz so'ragan barcha mahsulotlar do'konimizda mavjud.")
# else:
#     print(f"Quyidagi mahsulotlar do'konimizda yo'q: {mavjud_emas}")


# foydalanuvchilar = ["kimdir0000qz", 'qachoondir1999', 'futbolchiolim', 'nahotki4545', 'topdimqani']
# login = input("Login kiriting: ").strip()
# if login not in foydalanuvchilar:
#     print(f"Xush kelibsiz, {login}")
# else:
#     print("Login band, yangi login tanlang.")
    

# users = ["alisher1983", "aziza", "yasina", "umar"]

# login = input("Yangi login tanlang: ")

# if login in users:
#     print("Login band, yangi login tanalng!")
# else:
#     print("Xush kelibsiz!")   

# son = int(input("Son kiriting: "))

# for n in range(2,11):
#     if  son % n == 0:
#         print(f"Son {n} ga qoldiqsiz bo'linadi.")
#     else:
#         print("Yo'q, bo'linmaydi.")
    