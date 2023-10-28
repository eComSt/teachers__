N = int(input('Введите количество учеников:'))
data = []
for i in range(N):
    line = input('Введите ИМЯ БАЛЛ1 БАЛЛ2 БАЛЛ3:').split()
    data.append(line)
sub_1 = 0
sub_2 = 0
sub_3 = 0
for line in data:
    sub_1 += int(line[1])
    sub_2 += int(line[2])
    sub_3 += int(line[3])
    summ = int(line[1]) + int(line[2]) + int(line[3])
    print(f'Сумма баллов ученика {line[0]}: {summ}')
print(f'Средний балл по предмету 1: {sub_1/N}')
print(f'Средний балл по предмету 2: {sub_2/N}')
print(f'Средний балл по предмету 3: {sub_3/N}')