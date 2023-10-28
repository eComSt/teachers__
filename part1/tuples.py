tup = tuple()
tup_1 = ()
tup_2 = (1,2,3,4,5)
# print(tup_2[2:0:-1])
# print(type(tup), type(tup_1), type(tup_2))
# print(tup)
# print(tup_1)
# print(tup_2)
tup_3 = tuple([1,4,2,4,5,6,7,5,6])  # преобразование списка в кортеж
# print(tup_3)
tup_4 = tuple('Hello')  # преобразование строки в кортеж
# print(tup_4[1])
tup_5 = ([1,2,3,4,5,6],{1,2,4},{1:2,3:4}) 
# print(tup_5)
tup_5[0][0]=100
tup_5[1].add(100)
tup_5[2][1]=100
# print(tup_5)
tup_6 = (1,2,3,4,5,6,7,8,9,10)
a,b,c,_,_,_,_,_,_,_ = tup_6
# for i in tup_6:
#     print(i)
# a = tup_6[0]
# b = tup_6[1]
# c = tup_6[2]
# print(a)
# print(b)
# print(c)
tup_7 = (1,2,3,1)
# print(tup_7.count(1))
# print(tup_7.index(1))
tup_8 = tup_6 + tup_7
print(tup_8)
print(tup_7*2)