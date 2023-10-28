my_set = set()
my_set2 = {1,2,3}
my_set3 = {}
# print(type(my_set), type(my_set2), type(my_set3))
my_set.add(1)
my_set.add(2)
my_set.add(3)
# print(my_set)

my_set.discard(3)
my_set.discard(2)
my_set.remove(1)
# print(my_set)

for i in range(100):
    my_set.add(i)
# print(my_set)
my_set.clear()
# print(my_set)


my_grades = {3, 4, 5}
your_grades = {2, 4, 5}

# intersection() - пересечение множеств
# print(my_grades.intersection(your_grades))
# print(your_grades.intersection(my_grades))

# union() - объединение множеств
# print(my_grades.union(your_grades))

# difference() - вычитание множеств
diff_grades = your_grades.difference(my_grades)
# Методы intersection(), union(), difference() не меняют исходные множества, а создают новое множество
# print(diff_grades)
# Методы intersection_update(), update(), difference_update() работают также, как их аналоги, но меняют исходное множество
# my_grades.intersection_update(your_grades)
# print(my_grades)
# my_grades.update(your_grades)
# my_grades.difference_update(your_grades)

my_list = [1, 2, 3, 3, 1, 2, 4, 5]
# print(set(my_list))

str1 = 'I love cats'
str2 = 'c a t s'
# # issubset() - метод, проверяющий являются ли одно множество подмножеством другого
if set(str2).issubset(str1):
    print('Да')
else:
    print('Нет')

# issuperset() - метод, проверяющий, является ли одно множество супер-множеством для другого
if set(str1).issuperset(str2):
    print('Да')
else:
    print('Нет')
n = int(input("Введите N"))
result = set()
for i in range(1, n + 1):
    result.add(i)

while True:
    ask = input("Введите числа через пробел")
    if ask == 'HELP':
        print(result)
        break
    else:
        ask_set = set()
        for elem in ask.split():
            ask_set.add(int(elem))
    answer = input()
    if answer == 'YES':
        result.intersection_update(ask_set)
    elif answer == 'NO':
        result.difference_update(ask_set)