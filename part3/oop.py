class Car:
    mark = "Mercedes"
    color = "Black"
    model = "AMG"
    speed = 0

my_car_1 = Car()
my_car_2 = Car()
Car.speed  = 100
print(my_car_1)
print(type(my_car_1))
my_car_1.color = "White"
Car.color = "Blue"
print(f'Марка автомобиля:{my_car_1.mark}')
print(f'Модель автомобиля: {my_car_1.model}')
print(f'Цвет автомобиля:{my_car_1.color}')
print(f'Текущая скорость:{my_car_1.speed}')
print("_"*15)
print(f'Марка автомобиля:{my_car_2.mark}')
print(f'Модель автомобиля: {my_car_2.model}')
print(f'Цвет автомобиля:{my_car_2.color}')
print(f'Текущая скорость:{my_car_2.speed}')
print("_"*15)
print(f'Марка автомобиля:{Car.mark}')
print(f'Модель автомобиля: {Car.model}')
print(f'Цвет автомобиля:{Car.color}')
print(f'Текущая скорость:{Car.speed}')
