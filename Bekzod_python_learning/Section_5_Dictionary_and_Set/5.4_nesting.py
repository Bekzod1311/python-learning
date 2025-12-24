# "Nesting" in Python refers to placing one programming construct inside another, 
# typically used with loops, conditional statements (if/else), 
# and data structures like lists and dictionaries. This allows for complex logic and handling multidimensional data. 

# car0 = {
#     'model':'lacetti', 'rang':'oq',
#     'yil':2018, 'narx':13000,
#     'km':50000, 'korobka':'avtomat'
#     }
# car1 = {
#     'model':'nexia 3', 'rang':'qora',
#     'yil':2015, 'narx':9000,
#     'km':89000, 'korobka':'mexanika'
#     }
# car2 = {
#     'model':'gentra', 'rang':'qizil',
#     'yil':2019, 'narx':15000,
#     'km':20000, 'korobka':'mexanika'
#     }
# Hard way:
# car = car0
# print(f"{car['model'].title()},\
#  {car['rang']} rangi,\
#  {car['yil']}-yil, {car['narx']}$")

# car = car1
# print(f"{car['model'].title()},\
#  {car['rang']} rangi,\
#  {car['yil']}-yil, {car['narx']}$")

# car = car2
# print(f"{car['model'].title()},\
#  {car['rang']} rangi,\
#  {car['yil']}-yil, {car['narx']}$")

# Easy way:
# cars = [car0, car1, car2] # lo'g'atlar r'yxati
# for car in cars:
#     print(f"{car['model'].title()},\
#  {car['rang']} rang,\
#  {car['yil']}-yil, {car['narx']}$")

# print(cars[0])
# print(cars[0]['model'])
# print(f"{cars[0]['rang'].title()} {cars[0]['model']}")



# malibus = []
# for n in range(10):
#     new_car = { # har bir yangi avto uchun lug'at yaratamiz
#         'model':'malibu',
#         'rang':None, # rangi noaniq
#         'yil':2020,
#         'narx':None, # narxi noaniq
#         'km':0,
#         'korobka':'avto'
#     }
#     malibus.append(new_car) # lug'atni ro'yxatga qo'shamiz

# for malibu in malibus[:3]:
#     malibu['rang'] = 'qizil'
# for malibu in malibus[3:6]:
#     malibu['rang']='qora'
# for malibu  in malibus[6:]:
#     malibu['rang']='qora'
#     malibu['korobka']='mexanika'

# for malibu in malibus:
#     if malibu['korobka'] == 'avto':
#         malibu['narx'] = 40000
#     else:
#         malibu['narx']=35000

# for malibu in malibus:
#     print(malibu.values())



# dasturchilar = {
#     'ali':['python', 'c++'],
#     'vali':['html', 'css', 'js'],
#     'hasan':['php', 'sql'],
#     'husan':['python', 'php'],
#     'maryam':['c++', 'c#']
# }

# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism.title()}:", end = " ")
#     for til in tillar:
#         print(f'{til.upper()} ', end =" ")



# hamkasblar = {
#     'ali':{'familiya':'valiyev',
#            'tyil':1995,
#            'malumot':'oliy',
#            'tillar':['python', 'c++']
#            },
#     'vali':{'familiya':'aliyev',
#             'tyil':2001,
#             'malumot':"o'rta maxsus",
#             'tillar':['html', 'css', 'js']
#             },
#     'hasan':{'familiya':'husanov',
#              'tyil':1999,
#              'malumot':'maxsus',
#              'tillar':['python', 'php']
#              }
# }

# for ism, info in hamkasblar.items():
#     print(f"\n{ism.title()} {info['familiya'].title()}, \n{info['tyil']}-yilda tu'gilgan. \nMa\'lumoti: {info['malumot']}. \nQuyidagi dasturlash tillarini biladi: ")
#     for til in info['tillar']:
#         print(til.upper())




# Practice:
# 1)
# person1 = {
#     'name':"cristiano",
#     'surname':'ronaldo',
#     'current club':'al nassr',
#     'prime':'real madrid',
#     'ballon dor':5,
#     'friends':['Pepe', 'Rooney', 'Benzema']
# }
# person2 = {
#     'name':"lionel",
#     'surname':'messi',
#     'current club':'inter miami',
#     'prime':'barcelona',
#     'ballon dor':8,
#     'friends':['Neymar', 'Suarez', 'De Paul']
# }
# person3 = {
#     'name':"robert",
#     'surname':'lewandowski',
#     'current club':'barcelona',
#     'prime':'bavaria',
#     'ballon dor':0,
#     'friends':['Muller', 'Roys', 'Neur']
# }
# person4 = {
#     'name':"neymar",
#     'surname':'junior',
#     'current club':'santos',
#     'prime':'barcelona',
#     'ballon dor':0,
#     'friends':['Messi', 'Mbappe', 'Suarez']
# }

# famous_people = [person1, person2, person3, person4]
# for p in famous_people:
    # name = p['name']
    # surname = p['surname']
    # cclub = p['current club']
    # prime = p['prime']
    # bdor = p['ballon dor']
    # print(f"{name.title()} {surname.title()} {cclub.upper()}da o'ynaydi. \nPrime davir: {prime.upper()}. \nBallon Dor: {bdor}ta.  \n",  end = ' ')

    # ism = p['name']
    # dostlar = p['friends']
    # print(f"\n{ism.title()}ning do'stlari:")
    # for dost in dostlar:
    #     print(dost)


# 2)
# filmlar = {
#     'Laziz':['King Kong', 'Terminator', 'Bad Guys'],
#     'Nasim':['Paper House', 'Batman', 'Star Wars'],
#     'Firdavs':['Gladiator', 'Avengers', 'Mission Impossible']
# }
# for ism, kinolar in filmlar.items():
#     print(f"\n{ism.title()}ning sevimli filmlari: ")
#     for kino in kinolar:
#         print(kino)


# 3)
davlatlar = {
    'xitoy':{
        'poytaxti':'pekin',
        'tili':'xitoy',
        'iqtisodi':'ikkinchi'
    },
    'amerika':{
        'poytaxti':'washington',
        'tili':'ingliz',
        'iqtisodi':'birinchi'
    },
    'rossiya':{
        'poytaxti':'moskva',
        'tili':'rus',
        'iqtisodi':'uchinchi'
    }
}
# for davlat, info in davlatlar.items():
#     print(f"\nDavlat nomi: {davlat.title()}:, \nPoytaxti: {info['poytaxti'].title()}, tili: {info['tili']}. \nDunyo iqtisodidagi o'rni: {info['iqtisodi']}.")
     
# country = input("Davlat nomini kiriting: ").lower()
# if country in davlatlar:
#     info = davlatlar[country]
#     print(f"\nDavlat nomi: {country.title()}, poytaxti: {info['poytaxti'].title()}, tili: {info['tili']}")
# else:
#     print("Bizda bu davlat haqida ma'lumot yo'q.")