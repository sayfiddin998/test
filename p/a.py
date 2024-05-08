
# import random
# def sontop1(x=10):
#     input(f"1 dan {x} gacha son oylang.man topaman: ")
#     a = 1
#     b = x
#     while True:
#         if a != b:
#             tahmin = random.randint(a,b)
#         else:
#             tahmin = a
#         jovob = input(f"siz {tahmin} sonini oyladingiz: togri (t),"
#                       f"men oylagan son bundan kataroq (+), yoki kichikroq (-)" .lower())
#         if jovob == "-":
#             b = tahmin - 1
#         elif jovob == "+":
#             a = tahmin + 1
#         else:
#             break
#     print("Topdim!")
# sontop1(20)

# soz = input('ortoqini gapi: ')
# print(soz)
# def oyin():
#     o = input('o`ylagan soningizni kiriting: ')
#     print(f'siz shu sondi oyladigiz {o}')

# import random
# def sontop2(x=10):
#     tasodifiy_son = random.randint(1,x)
#     print(f"Men 1 dan {x} gacha son oyladim. topa olasizmi?")
#     taxminlar = 0
#     while True:
#         taxminlar += 1
#         taxmin = int(input(">>>"))
#         if taxmin<tasodifiy_son:
#             print("xato. men oylagan son bundan kattaroq. Yana harakat qiling: ")
#         elif taxmin>tasodifiy_son:
#             print("xato. men oylagan son bundan kichikroq. Yana harakatqiling: ")
#         else:
#             break
#     return taxminlar
#     print(f"tabriklaymiz. {taxminlar} ta taxmin bilan topdingiz!")
# sontop2()

# soz = 'ikki'
# a = list(soz)
# b = ('i', 'k', 'k', 'i')
# print(a)
# print(b)
# if a == b:
#     print('polindrom')
# else:
#     print('polidrom emas')

# olma = 54
# odam = 5
# print(olma // odam)
# print(olma % odam)

# qoshish = input('>>> ').split('+')
# son1 = int(qoshish[0])
# son2 = int(qoshish[1])
# son3 = int(qoshish[2])
# print(son1 + son2 + son3)
# sovga = 260000
# a = int(input('a bola: '))
# b = int(input('b bola: '))
# c = int(input('c bola: '))
# d = int(input('d bola: '))
# e = int(input('e bola: '))
# summa = a + b + c + d +e
# if summa >= sovga:
#     print('yetadi')
# else:
#     print(summa)
#     print(f'{sovga - summa} yetmaydi')

# import random
# def sontop(x=10):
#     tasodifiy_son = random.randint(1,x)
#     print(f"Men 1 dan {x} gacha son oyladim. topa olasizmi?")
#     taxminlar = 0
#     while True:
#         taxminlar += 1
#         taxmin = int(input(">>>"))
#         if taxmin<tasodifiy_son:
#             print("xato. men oylagan son bundan kattaroq. Yana harakat qiling: ")
#         elif taxmin>tasodifiy_son:
#             print("xato. men oylagan son bundan kichikroq. Yana harakat qiling: ")
#         else:
#             break
#     print(f"tabriklaymiz. {taxminlar} ta urinish bilan topdingiz!")
# sontop(100)

# sonlar = input('Qoshish uchun misol: ').split('+')
# son1 = sonlar[0]
# son2 = sonlar[1]
# son3 = sonlar[2]
# print(int(son1) + int(son2) + int(son3))

# son1 = int(input('1-son: '))
# son2 = int(input('2-son: '))
# son3 = int(input('3-son: '))
# sonlar = []
# sonlar.append(son1)
# sonlar.append(son2)
# sonlar.append(son3)
# sonlar.sort()
# print(sonlar[1])

# son = input('son kiriting men uni ornini almashtirib qoyaman: ').split()
# a = son[0]
# b = son[1]
# print(int(b), int(a))

# son = input('son kiriting kvadradini topaman: ').split()
# a = son[0]
# print(int(a) * int(a))

# son = int(input('son kiriting: '))
# for i in range(son):
#     print(son * '() ')

# son = input('son: ').split()
# a = int(son[0])
# b = int(son[1])
# c = int(son[2])
# royxat = []
# royxat.append(a)
# royxat.append(b)
# royxat.append(c)
# royxat.sort()
# print(royxat[-1])

# oquvchilar = [160, 162, 164, 166, 168, 170, 172]
# boyi = int(input('boy: '))
# a = oquvchilar.index(boyi)
# print(oquvchilar[a+1])

# a = int(input('ketish vaqti: '))
# b = int(input('nechi soatga kechikdi: '))
# natija = a + b
# if natija >= 24:
#     print(natija - 24)
# else:
#     print(natija)

# son = input('son kiriting: ').split()
# a = int(son[0])
# b = int(son[1])
# natija = b - a + 1
# print(natija * 10)










