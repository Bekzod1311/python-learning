# car = {'model':'ferrari', 'rang':'qizil'}
# print(car['model']) # ferrari
# print(car['rang']) # qizil


# talaba = {'ism':'murod olimov', 'yosh':25, 't_yil':2000}
# print(f"{talaba['ism'].title()}, \n{talaba['t_yil']}-yilda tug'ilgan.\n{talaba['yosh']} yoshda.")

# car = {
#     'make':'GM',
#     'model':'Malibu',
#     'color':'Black',
#     'gear':'Automatic',
#     'year':2020,
#     'price':40000
#     }
# print(car['model'])

# get() method
# print(car['narx']) # KeyError when there is no such key
# narx = car.get('narx', 'Bunday kalit mavjud emas.')
# print(narx)

# motor = car.get('motor') 
# print(motor) # None

# Adding new pair
# talaba = {'ism':'murod olimov', 'yosh':25, 't-yil':2000}
# talaba['kurs'] = 4
# talaba['fakultet'] = 'informatika'
# print(talaba)

# Empty dictionary
# car = {}
# car['model'] = 'Mazda 6'
# car['color'] = 'Red'
# car["price"] = 40000
# # print(f"{car['color']} {car['model']}, {car['price']}$")

# car['price'] = 38000
# print(f"{car['color']} {car['model']}, {car['price']}$")

# Deleting the pair (del)
# car = {'model':'Malibu', 'color':'Black', 'price':40000}
# print(car)
# del car['color']
# print(car)
# del car['model']
# car['year'] = 2009
# car['make'] = 'General Motors'
# print(car)


# Practice
# batman = {
#     'name':'Batman',
#     'color':'Black',
#     'city':'Gotham'
# }

# superman = {
#     'name':'Superman',
#     'color':'Blue-red',
#     'city':'Metropolis'
# }
# iron_man = {
#     'name':'Iron Man', 
#     'color':'Red-gold',
#     'city':'New York'
# }
# capitan_amerika = {
#     'name':'Capitan Amerika', 
#     'color':'Blue-white-red',
#     'city':'New York'
# }
# print(f"We our heroes resume: {batman}, \n{superman}, \n{iron_man}, \n{capitan_amerika}")
# print(f"We our heroes resume: {batman['name']}, {batman['color']} in {batman['city']}")


# sevimli_taomlar = {
#     'dad':'Palov',
#     'mom':'Kabob',
#     'brother':'Pizza',
#     'sister':'Burgers',
#     'grandma':'soup'
# }
# print(f"Dadam {sevimli_taomlar['dad'].lower()}ni, \nonam {sevimli_taomlar['mom'].lower()}ni, \nakam esa {sevimli_taomlar['brother'].lower()}ni yaxshi ko'rishadi.")


# python = {
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
# word = input("Istalgan atamani kiriting: ").lower()
# # print(python.get(word, 'Bunday so\'z mavjud emas.'))
# tarjima = python.get(word)
# if tarjima == None:
#     print('Bunday so\'z mavjud emas.')
# else:
#     print(f"{word.title()} so'zi {tarjima} deb tarjima qilinadi.")