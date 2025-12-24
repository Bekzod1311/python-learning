# In Python, a string (str) is an immutable sequence of Unicode characters used for handling text. 
# They are a fundamental data type and are created by enclosing characters in single quotes ('...'), double quotes ("..."), 
# or triple quotes ("""...""" or '''...''') for multiline strings. 

state = 'Frag\'ona'
avto = "Nexia"

matn = "Men yangi telefon oldim"
print(matn)
# In Python 3, all strings are Unicode by default, represented by the str type. 
# In Python 2, a dedicated unicode type and a u prefix (e.g., u"text") were used to differentiate Unicode strings from byte strings (str). 



# Matnlar ustida amallar
ism = 'Ahmad'
print("Mening ismim " + ism)

ism = 'Ahad'
familiya = 'Qayum'
print(ism+familiya)
# To leavea a space between
ism = 'Ahad'
familiya = 'Qayum'
print(ism + " " + familiya)


# f-string
# We can use f-string to combine several texts and variables with (f"{matn1} {matn2}") way.
ism = "Elon"
familiya = "Musk"
ism_sharif = f"{ism} {familiya}"
print(ism_sharif)


fname = "James"
lname = "Bond"
matn = f"Salom, mening ismim {fname}, {fname} {lname}!"
print(matn)

tyil = 2002
print(f"Siz {tyil}da to'gilgansiz.")
print(f"Yoshingiz {2025-tyil} da")


# \t  --> to leave a open space
# \n  --> to start from a new line
print("Hello World!")
print("Hello \tWorld!")
print("Hello \nWorld!")
