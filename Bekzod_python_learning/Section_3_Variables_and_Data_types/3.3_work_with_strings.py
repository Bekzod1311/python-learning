# Python string methods are built-in functions used to manipulate and transform text data. 
# Strings in Python are immutable, meaning these methods return a new string with the modifications, 
# rather than changing the original string in place. 

# upper()
ism = "bekzod"
familiya = "khusanov"
ism_sharif = f"{ism} {familiya}"
print(ism_sharif.upper())

# lower()
ism = "Bekzod"
familiya = "Khusanov"
ism_sharif = f"{ism} {familiya}"
print(ism_sharif.lower())

# title()
ism_sharif = 'james bond'
print(ism_sharif.title())

# capitalize()
ism_sharif = 'james bond'
print(ism_sharif.capitalize())

# you can directly use these methods to texts that to variables
print('james bond'.upper())


# lstrip() --> to remove the space from beginning
# rstrip() --> to remove the space from end
# strip()  --> to remove the space from both beginning and end
meva = "      olma      "
print(meva)
print("Men " + meva.lstrip() + "ni yaxshi ko'raman")
# Men olma      ni yaxshi ko'raman
print("Men " + meva.rstrip() + "ni yaxshi ko'raman")
# Men olma      ni yaxshi ko'raman
print("Men " + meva.strip() +"ni yaxshi ko'raman")
# Men olmani yaxshi ko'raman

meva = meva.strip()
print("Men "+ meva +"ni yaxshi ko'raman")