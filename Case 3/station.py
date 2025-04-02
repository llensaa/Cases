import random as rd
import ru_local as ru

class Station:

    def __init__(self, name):
        self.name = name
        self.resources = 1000
        self.people = 200
        self.military = 50
        self.station_farm = 0
        self.station_factory = 0


    def display_info(self):
        print(f'\n{ru.NAME}: {self.name}')
        print(f'{ru.MULTYPURPOSE_UNITS}: {self.resources}')
        print(f'{ru.POPULATION}: {self.people}')
        print(f'{ru.MILITARY_POWER}: {self.military}')


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
        print(f'\nru.UPGRADING_CHOICE')
        while True:
            choice = input()
            match choice:
                case ru.FACTORY | ru.FACTORY_2:
                    self.station_factory += 1
                    break
                case ru.FARM | ru.FARM_2:
                    self.station_farm += 1
                    break
                case _:
                    print(ru.WRONG_CHOICE)
                    continue


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
        print(f'\n{ru.WINNER} - {winner.name}, {ru.LOSER} - {loser.name}.')
        return winner, loser
