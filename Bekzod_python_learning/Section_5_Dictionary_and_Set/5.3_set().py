# A Python set is an unordered collection of unique, 
# hashable elements. Sets are mutable, meaning you can add 
# or remove items after creation, but the individual elements themselves 
# must be immutable (e.g., numbers, strings, tuples; not lists or dictionaries). 

# sonlar = {1, 2, 3}
# print(sonlar)
# ismlar = {'alijon', 'valijon', 'boqijon'}
# print(ismlar)

# sonlar = {1, 2, 3, 3, 3, 4, 4, 4, 5, 6, 5}
# print(sonlar) # {1, 2, 3, 4, 5, 6}

# a = set() # empty set

# sonlar = {1, 2, 3, 3, 4, 5, 5, 6}
# print(sonlar[0]) # TypeError: 'set object is not subscriptable

# mevalar = ['olma', 'anjir', 'olma', 'uzum', 'olma', 'uzum']
# mevalar = set(mevalar)
# print(mevalar)

# mevalar = list(mevalar)
# print(mevalar)


# adding an element to set:
# .add() and .update()
# mevalar = {'anjir', 'olma', 'uzum'}
# mevalar.add("banan") # we are adding one element
# print(mevalar)
# mevalar.update(['anor', 'qovun'])
# print(mevalar)

# deleting an element to set:
# .discard() and .remove()
# mevalar = {'anjir', 'olma', 'uzum', 'banan', 'anor'}
# mevalar.discard('anjir')
# print(mevalar)
# mevalar.remove('banan')
# print(mevalar)

# mevalar.discard('ananas')
# print(mevalar) # not error
# mevalar.remove("nok")
# print(mevalar) # KeyErro: 'nok'

# sonlar = {1, 2, 3, 4, 5, 6}
# son = sonlar.pop()
# print(son)
# print(sonlar)

# | or .union()
# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
# C = A|B
# print(C)
# D = A.union(B)
# print(D)

# & or .intersection()
# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
# print(A&B)
# print(A.intersection(B))


# - or .difference()
# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
# print(A-B)
# print(B.difference(A))

# ^ or .symmetric_difference()
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
# print(A^B)
# print(A.symmetric_difference(B))


# Practice:
# 1)
# colors = {"red", 'blue', 'green'}
# colors.add('brown')
# colors.update(['black', 'white', 'gold'])
# print(colors)

# 2)
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# set3 = set1&set2
# print(sorted(set3))

# print(f"Farqlar: {set1.difference(set2)} va {set2-set1}")

# print(sorted(set2.symmetric_difference(set1)))

# 3)
# bozorlik = ['choy', 'non', 'kartoshka', 'tuxum', 'sut']
# mahsulotlar = ['non', 'sut', 'tuxum', 'olma', 'un', 'tuz']
# set1 = set(bozorlik)
# set2 = set(mahsulotlar)
# set3 = set1&set2
# set3 = list(set3)
# print(set3)
# set4 = set1-set2
# print(list(set4))
# set2.update(['choy', 'kartoshka'])
# print(list(set2))

