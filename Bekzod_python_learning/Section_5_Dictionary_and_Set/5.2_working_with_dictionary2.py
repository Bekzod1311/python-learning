# .items() method

# talaba = {
#     'ism':'alijon',
#     'familiya':'shamsiyev',
#     'yosh':22,
#     'fakultet':'matematika',
#     'kurs':5
# }

# # print(talaba.items())
# for kalit, qiymat in talaba.items():
#     print(f"Kalit: {kalit},")
#     print(f"Qiymat: {qiymat}")

# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310'
# }
# for k, q in telefonlar.items():
#     print(f"{k.title()}ning telefoni {q}.")


#  .keys() methodi
# mahsulotlar = {
#     'olma':10000,
#     'anor':20000,
#     'uzum':40000,
#     'anjir':25000,
#     'shaftoli':30000
# }
# print(mahsulotlar.keys())
# print('Do\'kondagi mahsulotlar:')
# for mahsulot in mahsulotlar:
#     print(mahsulot.title())

# bozorlik = ['anor', 'uzum', 'non', 'baliq']
# for m in mahsulotlar:
#     if m in bozorlik:
#         print(f"{m.title()} {mahsulotlar[m]} so'm")

# for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#         print(f"Kechirasiz, bizda {buyum} yo'q.")

# print("Do'konimizdagi mahsulotlar: ")
# for mahsulot in sorted(mahsulotlar):
#     print(mahsulot.title())


# .values() methodi
# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10',
#     'orif':'nokia 3310',
#     'hamida':'galaxy s9',
#     'maryam':'huawei p30',
#     'tohir':'iphone x',
#     'umar':'iphone x'
# }
# print(telefonlar.values())

# print("Foydalanuvchilarning telefonlar:")
# for telefon in telefonlar.values():
#     print(telefon)

# print("Foydalanuvchilarning telefonlari: ")
# for tel in set(telefonlar.values()):
#     print(tel)


# Practice:
# 1)
# python_izohli_lugati = {
#     'integer':'butun son',
#     'float':"o'nli son",
#     'string':'matn',  
#     'boolean':'True-False',
#     'if':'agar',
#     'else':"bo'lmasa",
#     'and':'va',
#     'or':'yoki',
#     'list':"lo'g'at",
#     'dictionary':"lo'g'at"
# }
# for k, q in sorted(python_izohli_lugati.items()):
#     print(f"'{k.title()}' ning tarjimasi '{q}' bo'ladi.")

# 2)
davlatlar = {
    "O'zbekiston":'Tashkent',
    'rossiya':'moskva',
    'fransiya':'parish',
    'germaniya':'berlin',
    'amerika':'washington'
}
# print("Davlatlar: ")
# for davlat in sorted(davlatlar):
#     print(davlat.upper())

# print("Davlatlarning poytaxtlari: ")
# for q in sorted(davlatlar.values()):
#     print(q.title())


# 3)
# davlat = input('Istalgan davlat nomini kiriting: ').lower()
# if davlat in davlatlar.keys():
#     print(f"{davlat.title()}ning poytaxti: {davlatlar[davlat].title()}")
# else:
#     print('Bizda bunday ma\'lumot yo\'q.')

# 4)
menu = {
    'osh':35000,
    'shashlik':24000,
    'sho\'rva':25000,
    'somsa':12000,
    'manti':10000,
    'lagmon':20000,
    'qozon kabob':70000,
    'xalisa':80000,
    'bishteks':25000,
    'salat':15000
}
taom1 = input("Birinchi taomni kiriting: ").lower()
taom2 = input('Ikkinchi taomni kiriting: ').lower()
taom3 = input("Uchinchi taomni kiriting: ").lower()
if taom1 in menu:
    print(f"{taom1.title()}ning narxi: {menu[taom1]} so'm")
else:
    print(f'Bizda {taom1} taom yo\'q.')
if taom2 in menu:
    print(f"{taom2.title()}ning narxi: {menu[taom2]} so'm")
else:
    print(f'Bizda {taom2} taom yo\'q.')
if taom3 in menu:
    print(f"{taom3.title()}ning narxi: {menu[taom3]} so'm")
else:
    print(f'Bizda {taom3} taom yo\'q.')