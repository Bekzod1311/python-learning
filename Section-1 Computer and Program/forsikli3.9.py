# for sikli
"""mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan']
for mehmon in mehmonlar:
    print(mehmon)"""
""" mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan']
for mehmon in mehmonlar:
    print(f"Hurmatli {mehmon},")
    print("Sizni 20-mart kuni nahorgi oshga taklif qilamiz.")
    print("Hurmat bilan, men!") """
""" mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan']
for mehmon in mehmonlar:
    print(f"Hurmatli {mehmon},")
    print("Sizni 20-Mart kuni nahorgi oshga taklif qilamiz.")
        # keyingi qator ham sikl ichida yoziladi.
    print("Hurmat bilan men!") """
""" cars = ['Nexia', 'Damas', 'Tico']
for car in cars:
    print(car.title()) # sikl sharti
    print("Ko'rganlar qilar havas!") # sikldan keyingi kod """
"""sonlar = list(range(1, 11))
for son in sonlar:
    print(f"{son} ning kvadrati {son**2} ga teng")
"""
"""sonlar = list(range(11)) # 1 dan 11 gacah sonlar ro'yxati
sonlar_kvadrati = [] # bo'sh ro'yxat
for son in sonlar:
    sonlar_kvadrati.append(son**2)
print(sonlar)
print(sonlar_kvadrati)"""

""" dostlar = [] # bo'sh ro'yxat
print("Beshta eng yaqin do'stlaringiz:")
for n in range(5):
    dostlar.append(input(f"{n+1}-do'stingiz: "))
print(dostlar)""" 
#Amaliyot
""" filmlar = ['Ford vs Ferrari', 'Furry', 'Avengers', 'Transformers', 'Gladiator']
son = []
for x in filmlar:
    son =  filmlar[:]
    print(f"Men bu {x}ni ko'rganman")
print(f"Kod {len(son)} marta takrorlandi") """
""" sonlar = list(range(100))
toq_sonlar = sonlar[11:100:2]
for son in toq_sonlar:
    print(f"Bu {son} ning kubi = {son**3}") """
"""kinolar = [] #bo'sh ro'yxat
print("Beshta eng yaxshi kino: ")
for n in range(5):
    kinolar.append(input(f"{n+1}-kino: "))
print(kinolar)  """  
""" s_odamlar = int(input("Bugun nechta odam bilan gaplashdiz? "))
ismlar = []
for n in range(s_odamlar):
    ismlar.append(input(f"Ism: "))
print(s_odamlar)
print(ismlar) """






























