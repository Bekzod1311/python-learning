# Python lists are a built-in, versatile data structure used to store 
# an ordered collection of items in a single variable. 
# They are defined using square brackets [] and can contain elements of different data types, 
# including numbers, strings, Booleans, and even other lists. 

mevalar = ["olma", 'anjir', 'shaftoli', "o'rik"]
narxlar = [12000, 18000, 10900, 22000]
sonlar = ['bir', 'ikki', 3, 4, 5]  # combined
ismlar = [] # empty list


# Indexed: The first element has an index of 0, the second 1, and so on. 
# Negative indices count from the end of the list (e.g., -1 refers to the last item).
# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
# print("Birinchi meva: ", mevalar[0])
# print("Ikkinchi meva: ", mevalar[1])
# print("Ozirgi meva: ", mevalar[-1])

# mevalar = ["olma", 'anjir', 'shaftoli', "o'rik"]
# print("Birinchi meva: ", mevalar[0].title())
# print("Ikkinchi meva: ", mevalar[1].upper())

# narxlar = [12000, 18000, 10900, 22000]
# print(narxlar[2]+narxlar[3])

# sonlar = [10, 112, 345, -23, 446, 61, -45, 56, -34]
# print(sonlar[-1]) # -1 index --> the last element of the list.

# narxlar = [12000, 18000, 10900, 22000]
# narxlar[0] = 13000 # changing the first element to  13000
# narxlar[2] = 11000
# narxlar[3] = narxlar[3] +2000

# narxlar[4] = 20000 # IndexError: list assignment index out of range
# print(narxlar) 

# append()
# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
# mevalar.append("tarvuz")  # we are adding another new element to list
# print(mevalar)

# cars = []
# cars.append('Lacetti')
# cars.append('Nexia 3')
# cars.append('Cobalt')
# print(cars)

# insert()
# cars = ['Lacetti', 'Nexia 3', 'Cobalt']
# print(cars)
# cars.insert(0,'Malibu')
# print(cars)
# cars.insert(2, 'Damas')
# print(cars)


# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik", 'anor']
# del mevalar[1] # we are deleting the second element in this list
# print(mevalar)

# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik", 'anor']
# mevalar.remove('shaftoli')
# print(mevalar)
# hayvonlar = ['it', 'mushuk', 'sigir', 'quyon', 'mushuk']
# hayvonlar.remove('mushuk')
# print(hayvonlar)

# pop()
# bozorlik = ["yog'", 'un', 'piyoz', 'banan', "go'sht"]
# mahsulot = bozorlik.pop(3) # 4 - elementni sug'urib olamiz
# print("Men " + mahsulot + " sotib oldim.")
# print("Olinmagan mahsulotlar: ", bozorlik)

# numbers = [1, 2, 3, 4, 5 ]
# print(numbers)
# numbers.pop()
# print(numbers)



# Practice

# ismlar = ["Laziz", "Nasim", "Firdavs"]
# print(f"Salom {ismlar[0]}, ishlaring yaxshimi?")
# print(f"{ismlar[1]} va {ismlar[2]}lar o'rtoqlar.")
# print(f"{ismlar[-1]} g'ildirakni g'izillatib g'ildiratdi.")

# sonlar = [1, 5, -6, 0, 9.0]
# print(sonlar[0]+sonlar[1])
# print(sonlar[-1]*sonlar[2])
# print(sonlar)
# sonlar[3] = 781
# sonlar[-1] = sonlar[-1] + 10
# sonlar.insert(0, 999)
# print(sonlar)

# t_shaxslar = ['Yuliy Sezar', 'Napoleon', 'Amir Temur', 'Chingizxon']
# z_shaxslar = ['Elon Musk', 'Jeff Bezos', 'Mark Sukerberg']
# name1 = t_shaxslar.pop(1)
# name2 = z_shaxslar.pop(2)
# print(f"Men tarixiy shaxslardan {name1} bilan, \nzamonaviy shaxslar bilan esa {name2} bilan \nsuhbat qilishni istar edim.")

friends = []
friends.append('Laziz')
friends.append('Nasim')
friends.append('Firdavs')
friends.append('Allayar')
friends.append('Mirshat')
print(friends)

# friends.remove('Mirshat')
# print(friends)
# friends.insert(0, 'Devdas')
# friends.insert(2, 'Hasif')
# friends.insert(-1, 'Ahror')
# print(friends)

yangi_mehmonlar = []
guy = friends.pop(2)
yangi_mehmonlar.append(guy)
print(yangi_mehmonlar)