# A for loop in Python is a control flow statement used for iterating over a sequence (such as a list, tuple, string, or range) 
# or other iterable objects. It executes a block of code once for each item in the sequence, making it ideal 
# for repetitive tasks with a known number of iterations. 

# mehmonlar = ["Ali", 'Vali', 'Hasan', 'Husan', 'Olim']
# for mehmon in mehmonlar:
#     print(mehmon)

# mehmonlar = ["Ali", 'Vali', 'Hasan', 'Husan', 'Olim']
# for mehmon in mehmonlar:
#     print(f"Hurmatli {mehmon},")
#     print("Sizni 20-Mart kuni nahorgi oshga taklif qilamiz.")
#     print("Hurmat bilan , Palonchayevlar oilasi.")

# cars = ['nexia', 'tico', 'damas']
# for car in cars:
#     print(car.title())
# print("Ko'rganlar qilar havas.")



# sonlar = list(range(1,11))
# for son in sonlar:
#     print(f"{son} ning kvadrati {son**2} ga teng. ")


# sonlar = list(range(1,11))
# sonlar_kvadrati = []
# for son in sonlar:
#     sonlar_kvadrati.append(son**2)
# print(sonlar)
# print(sonlar_kvadrati)


# for and input()
# friends = []
# print("Beshta eng yaqin do'stingizni ismini kiriting: ")
# for n in range(1,6):
#     friends.append(input(f"{n}- ismini kiriting: "))
# print(friends)



#Practice:
# ismlar = ['Ronaldo', 'Messi', 'Neymar', 'Lewandowski', 'Benzema' ]
# for ism in ismlar:
#     print(f"Eng zo'r futbolchi: {ism}")
#     # for n in range(1,6):
#     #     print(f"{n} - o'rinda: {ism}")
# # print(ismlar)
# print("Kod", len(ismlar), " marta takrorolandi.")

# numbers = list(range(11,100,2))
# print(numbers)
# toq_kub_sonlar = []
# for n in numbers:
#     toq_kub_sonlar.append((n**2)*n)
# print(toq_kub_sonlar)


# kinolar = []
# print("Eng yoqtirgan beshta kinoni nomini kiriting: ")
# for n in range(5):
#     kinolar.append(input(f"{n+1}-kino nomini kiriting: "))
# print(kinolar)


# people = []
# print("Bugun nechta inson bilan gaplashdingiz: ")
# num = int(input("Raqamni kiriting: "))
# for n in range(num):
#     people.append(input(f"{n+1} - ismini kiriting: "))
# print(people)