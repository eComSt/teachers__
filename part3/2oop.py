from pprint import pprint
class Car:
    def __init__(self, mark = "Mercedes", 
                model ="AMG", color = "Black",
                speed = 0):
        self.mark = mark
        self.color = color
        self.model = model
        self.speed =  0
    def set_power_engine(self,power):
        self.power_engine = power
    def show_info(self):
        print(f'Марка: {self.mark}')
        print(f'Модель: {self.model}')
        print(f'Цвет: {self.color}')
        print(f'Текущая скорость: {self.speed}')
        print('_'*15)
    def get_attributes(self):
        return self.mark, self.model, self.color, self.speed
    def __del__(self):
        print('Сработал метод __del__')
my_car_1 = Car()
del my_car_1
my_car_1.color = "Red"
my_car_2 = Car("Toyota", "Corolla", "White", 100)
my_car_1.show_info()
my_car_2.show_info()
my_car_1.set_power_engine(199)
# attrs = my_car_1.get_attributes()
