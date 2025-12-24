# Python has three primary built-in number types: integers (int), 
# floating-point numbers (float), and complex numbers (complex). 
# These are used to represent numeric values and perform mathematical operations. 

# Integers - Butun sonlar
# a = 20 # Sonlar musbat
# b = -30 # Manfiy 
# c = 0 # 0 ga teng
# d = a + b
# print(d)


# Calculate the area of the square
# kvdrt_tmni = 20 # The measurement of side of square is 20
# kvdrt_yuzi = kvdrt_tmni ** 2
# print(kvdrt_yuzi)


# Floats - o'nlik sonlar
# pi = 3.14159 # float number
# radius = 10 # integer number
# diametr = 2*radius
# print("Aylananing uzunligi ", pi*diametr, "ga teng")

# From integer to float
# a = -20
# b = 40
# c = b/a
# print(c)

# a = 2 
# b = 3.0
# print(a+b) # 5.0 float
# print(a*b) # 6.0 float
# print(a**b) # 8.0 float
# print(2*(a+b)) # 10.0 float

# Entering long numbers
 # _
# aholi = 33_580_000
# print(f"O'zbekiston aholisi {aholi}dan ortiq")

# Constant
PI = 3.14159 # constant
radius = 21.



# x, y, z = 10, -7.25, -30
# yosh, ism = 36, "Olimjon"
# print(f"{ism.title()} {yosh} yoshda")



# ism = 'Jobir'
# yosh = 36
# xabar = ism + ' ' + yosh 'yoshda'
# print(xabar)  #  TyoeError

# We need to use typecasting

# str()
# int()
# float()
# ism = "Jobir"
# yosh = 36
# xabar = ism + ' ' + str(yosh) + ' yoshda'
# print(xabar)

# To check the type
# type()
# ism = 'Jobir'
# yosh = 36
# print(type(ism)) # class 'str'
# print(type(yosh)) # class 'int'


# input() and numbers
# We ask user his/her age
# t_yil = input("To'g'ilgan yilingizni kiriting: ")
# User will input his/her age
# yosh = 2025-t_yil
# Out = the age
#print("Siz "+yosh+ " yoshda ekansiz") #TypeError: unsupported operand type(s) for -: 'int' and 'str'

# t_yil = int(input("To'g'ilgan yilingizni kiriting: "))
# yosh = 2025-t_yil
# print("Siz "+str(yosh)+" yoshda ekansiz.")

# Practice
# 1)
# son = int(input("Son kiriting: "))
# sonkv = son**2
# sonkub = son * (son**2)
# print(f"Sonning kvadrati teng  {sonkv} ga, \nsonning kubi esa teng {sonkub} ga.")

# 2) 
# age = int(input("Yoshingizni kiriting: "))
# t_yil = 2025 - age
# print(f"Siz {t_yil}-yilda to'g'ilgansiz.")

# 3)
# son1 = int(input("Birinchi son: "))
# son2 = int(input("Ikkinchi son: "))
# son_yig = son1+son2
# son_ay = son1-son2
# son_kop = son1*son2
# son_bol = son1/son2
# print(f"Kiritilgan sonlarning ko'paytmasi: {son_kop}, \nyig'indisi {son_yig}, \nayirmasi {son_ay}, \nbo'linmasi {son_bol}ga teng.")