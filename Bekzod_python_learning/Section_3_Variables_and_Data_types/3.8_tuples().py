# tomonlar = (20, 30, 55.2)
# print(tomonlar)

# toys = ('bus', 'car', 'bear', 'dino', 'snake', 'lizard')
# print(toys)
# print(toys[0])
# print(toys[-1])
# print(toys[2:5])

# toys[30] = 'dragon' # TypeError: 'tuple object does not support item assignment.

# # o'zgarmas ro'yxat yaratamiz
# toys = ('bus', 'car', 'bear', 'dino', 'snake', 'lizard')
# # o'zgarmas ro'yxatni oddiy ro'yxatga almashtiramiz
# toys = list(toys)
# # ro'yxatga o'zgartitishlar kiritamiz
# toys.append('dragon')
# toys.remove('bus')
# toys[1] = "mcqueen"
# # Ro'yxatni qaytadan o'zgarmas ro'yxatga (Tuple) aylantiramiz
# toys = tuple(toys)
# print(toys)



#Practice
# davlatlar = ("O'zbekiston", 'Amerika', 'Xitoy', 'Janubiy Korea', 'Italiya', 'Qatar', "Avstralia", 'Malaysia')
# print(davlatlar)
# print(len(davlatlar))
# print(sorted(davlatlar))
# print(sorted(davlatlar, reverse = True))
# print(davlatlar)
# yurtlar = list(davlatlar)
# yurtlar.reverse()
# print(yurtlar)
# yurtlar.sort(reverse = True)
# print(yurtlar)


# sonlar = list(range(120,1200))
# print(sum(sonlar))
# print(max(sonlar)-min(sonlar))
# print(len(sonlar))
# print(sonlar[0:20])
# print(sonlar[540:560])
# print(sonlar[-20:1081])


# taomlar = ['somsa', 'osh', 'manti', 'shashlik', "sho'rva"]
# nonushta = taomlar[:]
# nonushta.remove('somsa')
# nonushta.remove('shashlik')
# nonushta.append("Sut")
# nonushta.append('Tuxum')
# print(taomlar)
# print(nonushta)
# nonushta = tuple(nonushta)
# nonushta[0] = 'qaymoq va non' # TypeError: 'tuple' object does not support item assignment