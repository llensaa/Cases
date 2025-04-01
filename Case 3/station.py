import random as rd

class Station:

    def __init__(self, name):
        self.name = name
        self.resources = 1000
        self.people = 200
        self.military = 50
        self.station_farm = 0
        self.station_factory = 0


    def display_info(self):
        print(f'\nНазвание: {self.name}')
        print(f'Универсальные единицы: {self.resources}')
        print(f'Население: {self.people}')
        print(f'Военная мощь: {self.military}')


    def searching(self):
        '''
        Function, station is going to search for resources
        :return: None
        '''
        self.resources -= 200
        self.people -= 10
        probability = rd.randint(1, 100)
        if probability > 20:
            self.resources += 350
            self.people += 10


    def upgrading(self):
        '''
        Function, upgrading the station
        :return: None
        '''
        self.resources -= 20
        choice = input('Какое предприятие вы хотите строить: ферму или фабрику?')
        while True:
            match choice:
                case 'Фабрика' | 'фабрика':
                    self.station_factory += 1
                    break
                case 'Ферма' | 'ферма':
                    self.station_farm += 1
                    break


    def battle(self, enemy):
        '''
        Function, station fights with enemy station
        :param enemy:
        :return: None
        '''
        self_power = 0.7 * self.military + 0.3 * self.people
        enemy_power = 0.7 * enemy.military + 0.3 * enemy.people
        if self_power > enemy_power:
            winner, loser = self, enemy
        else:
            winner, loser = enemy, self
        winner.resources += 20
        loser.resources -= 30
        loser.people -= 40
