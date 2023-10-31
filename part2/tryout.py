
# if num_2 == 0:
#     print('Делить на ноль нельзя!')
# else:
#     print(num_1 / num_2)
try:
    num_1 = int(input('Введите первое число:'))
    num_2 = int(input('Введите второе число:'))
    result = num_1 % num_2
except ZeroDivisionError:
    num_2 = int(input('Делить на ноль нельзя, введите новое число:'))
except ValueError:
    print('Введено некорректны значения!')
    num_1 = int(input('Введите первое число:'))
    num_2 = int(input('Введите второе число:'))
except:
    print('Неизвестная ошибка!')
finally:
    result = num_1 % num_2
    print(f'Остаток от деления: {result}')