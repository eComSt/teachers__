from random import randint
def gen():
    return (randint(1,10), randint(1,10), randint(1,10))
def math_op(a,b,c):
    summ = a+b+c
    srednee = summ/3
    mult = a*b*c
    return summ, srednee, mult

summ, sr, mult = math_op(1,2,4)
vals = (1,2,4)
summ, sr, mult = math_op(vals[0], vals[1], vals[2])
summ, sr, mult = math_op(*vals)
# print(summ)
# print(sr)
# print(mult)
# for _ in range(10):
#     print(math_op(*gen()))

# empty_tuple = ()
# if empty_tuple:
#     print('Yes')
# else:
#     print('No')
tup_9 = (1,)
print(tup_9,type(tup_9))