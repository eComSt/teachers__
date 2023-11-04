class SportCar:
    mark = ''
    model  = ''
    power = 0
    max_speed = 0

cars = []
for _ in range(3):
    car = SportCar()
    car.mark = input('Введите марку машины:')
    car.model = input('Введите модель машины:')
    car.power = int(input('Введите мощность машины:'))
    car.max_speed = int(input('Введите максимальную скорость машины:'))
    cars.append(car)
    print('_'*15)
for car in cars:
    print(car.mark, car.model, car.power, car.max_speed)
    print('_'*15)
