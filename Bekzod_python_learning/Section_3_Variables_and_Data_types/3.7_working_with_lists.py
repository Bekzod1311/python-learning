# sort()  --> sorting
# cars = ['bmw', 'volvo', 'gm', 'tesla', 'audi']
# cars.sort()
# print(cars)

# cars = ['bmw', 'mercedes', 'volvo', 'gm', 'tesla', 'audi']
# cars.sort(reverse =True)
# print(cars)

# mehmonlar = ['Odil', 'Hamid', 'Temur', 'Avazbek', 'Farrux']
# print("sorted() qaytargan ro'yxat ", sorted(mehmonlar))
# print("Asl ro'yxat o'zgarmas qoladi:" , mehmonlar)

# print(sorted(mehmonlar, reverse = True))

# ages = [12, 98, 34, 65, 34, 76, 11]
# ages.sort()
# print(ages)
# print(sorted(ages, reverse = True))


# reverse()
# fruits = ['pear', 'banana', 'apple', 'watermelon', 'lemon']
# fruits.reverse()
# print(fruits)

# len()
# fruits = ['pear', 'banana', 'apples', 'watermelon', 'lemon']
# print("Elementlar soni: ", len(fruits))


# range()
# sonlar = list(range(0,10))
# print(sonlar)

# juft_sonlar = list(range(0, 20, 2)) # 0 dan 20 gacha 2 qadam bilan
# toq_sonlar = list(range(1,20, 2))
# print("Juft sonlar: ", juft_sonlar)
# print("Toq sonlar: ", toq_sonlar)

# min() -- to find the smallalest number
# max() -- to find the biggest number
# sum()  -- to find the sum of the numbers
# narxlar = [12000, 225000, 23456, 9800, 5600, 9934, 32874]
# arzon = min(narxlar)
# qimmat = max(narxlar)
# jami = sum(narxlar)
# print("Eng arzon narx: ", arzon, "\neng qimmat narx: ", qimmat, "\nyi'gindisi: ", jami)


# cars = ['bmw', 'volvo', 'gm', 'toyota', 'tesla', 'audi']
# my_cars = cars[0:3] # 0 dan boshlab 3 ta element
# print(my_cars)
# print(cars[2:5])
# print(cars[:4])
# print(cars[2:])


# sonlar = [1, 2, 3, 4, 5]
# sonlar2 = sonlar
# sonlar2.append(6)
# sonlar2.append(7)
# print("Bu sonlar ro'yxati:", sonlar)
# print("Bu sonlar2 ro'yxati:", sonlar2)

# sonlar = [1, 2, 3, 4, 5]
# sonlar2 = sonlar[:]
# sonlar2.append(6)
# sonlar2.append(7)
# print("Bu sonlar ro'yxati: ", sonlar)
# print("Bu sonlar2 ro'yxati: ", sonlar2)