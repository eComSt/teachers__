name = input("Введите имя:")
file = open("log_calc.txt", "a",encoding="utf-8")
file.write(f'{name}\n')
while True:
    try:
        num_1 = int(input('Введите первое число:'))
        oper = input('Введите операцию + - * / ** // %:')
        num_2 = int(input('Введите второе число:'))
        file.write(f'{num_1} {oper} {num_2}\n')
        result = eval(f'{num_1}{oper}{num_2}')
    except ZeroDivisionError:
        num_2 = int(input('Делить на ноль нельзя, введите новое число:'))
        file.write("На ноль делить нельзя\n")
        file.write(f'Введено новое число: {num_2}\n')
    except ValueError:
        print('Введены некорректные значения!')
        num_1 = int(input('Введите первое число:'))
        num_2 = int(input('Введите второе число:'))
        file.write("Введены некорректные значения!\n")
        file.write(f'Введены новые числа: {num_1} и {num_2}\n')
    except SyntaxError:
        oper = input('Введите корретную операцию (+ - * / ** // %):')
        file.write("Введены некорректная операцию!\n")
        file.write(f'Введена новая операция: {oper}\n')
    finally:
        result = eval(f'{num_1}{oper}{num_2}')
        print(f'Результат {num_1}{oper}{num_2} = {result}')
        file.write(f'Результат {num_1}{oper}{num_2} = {result}\n')
        is_continue = input("Продолжать? y/n:")
        if is_continue == "n":
            print("Good bye!")
            file.write('-'*15+'\n')
            file.close()
            break
        print("-"*15)