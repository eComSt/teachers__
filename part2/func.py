words  = ['four','sixteen', 'twentyfour','eleven','nineteen','sdfsdfsdfsdfsdfsdfsdfsdfsdf']
word = max(words, key=len)
# print(word)
def double(n):
    return n*2
double = lambda n: n*2
# print(double(21))

data = ['1','32','17','42','13']
d = max(data, key=lambda x: int(x))
# d = max(data, key=int)
# print(d)
new_data = list(map(int, data))
# print(new_data)

base = [1,2,5,6]
exp =[2,3,4,5]
ans = list(map(lambda x,y: x**y, base, exp))
# print(ans)
colors = ['красный', 'синий', 'оранжевый', 'желтый', 'зеленый','белый']
colors_new = [c for c in colors if len(c)>5]
colors_new = list(filter(lambda x: len(x)>5, colors))
# print(colors_new)

words = ['','шалаш','кот','топот','бег']
words_new = list(filter(lambda x: x == x[::-1], words))
# print(words_new)

from functools import reduce
numbers = [1,2,3,4,5]
result = reduce(lambda x,y: x*y, numbers)
# print(result)

numbers = [1,2,3,4,5]
numbers2 = [2,3,4,5,6]
numbers3 = [3,4,5,6,7,8]
numbers4 = [1,2,3,4,5,6]
for i in zip(numbers,numbers2,numbers3,numbers4):
    print(i)
print("-"*15)
from itertools import zip_longest
for i in zip_longest(numbers,numbers2,numbers3,numbers4):
    print(i)