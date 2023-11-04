class Hero:
    def __init__(self, name, health, damage, defense):
        self.name = name
        self.health = health
        self.damage = damage
        self.defense = defense
    def get_status(self):
        print(f'Имя: {self.name}')
        print(f'Здоровье:{self.health}')
        print(f'Урон: {self.damage}')
        print(f'Защита:{self.defense}')
        print('--------------------------------------------------')
    def increase_defense(self):
        if self.defense * 1.5 < 100:
             self.defense *= 1.5
        else:
            print('Достигнут максимальный уровень защиты!')
        print(f'Текущий уровень защиты: {self.defense}')
        print('--------------------------------------------------')
    def make_damage(self, enemy):
        print(f'Атака по персонажу {enemy.name}!')
        print('--------------------------------------------------')
        enemy.get_damage(self.damage)
    def get_damage(self, damage):
        absobrbed_damage = damage*self.defense/100
        damage = damage - absobrbed_damage
        print(f'Получено {damage} урона!')
        print('--------------------------------------------------')
        self.health -= damage
hero_1 = Hero('Superman', 100, 10, 5)
hero_2 = Hero('Batman', 100, 5, 10)
for _ in range(100):
    hero_1.increase_defense()
    hero_1.make_damage(hero_2)
    hero_2.increase_defense()
    hero_2.make_damage(hero_1)
hero_1.get_status()
hero_2.get_status()