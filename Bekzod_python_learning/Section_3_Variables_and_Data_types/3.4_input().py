# In Python, user input is primarily handled using the built-in input() function, 
# which pauses the program's execution and reads a line of text from the user via the keyboard 
# when the Enter key is pressed. The input is always returned as a string data type by default. 

# ism = input("Ismingiz nima? ")
# print("Assalomu alaykum " + ism)

# ism = input("Ismingiz nima?\n ")
# print(f"Assalomu alaykum {ism.title()}.")

#Practice
# 1) Create variables
# kocha = "Bog'bon"
# mahalla = "Sag'bon"
# tuman = "Bodomzor"
# viloyat = "Samarqand"

# # 2) Print them out:
# print(f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")

# 3) Ask user to input: 
# variables
kocha = input("Ko'cha nomini kiriting: ")
mahalla = input("Mahalla nomini kiriting: ")
tuman =  input("Tuman nomini kiriting: ")
viloyat =  input("Viloyat nomini kiriting: ")

#  print 
# print(f"{kocha.title()} ko'chasi, \n{mahalla.title()} mahallasi, \n{tuman.title()} tumani, {viloyat.title()} viloyati")

yangi_manzil = f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"
print(yangi_manzil.title())