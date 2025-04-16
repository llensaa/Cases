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

    def result_value(self):
        return (self.resources * self.military * self.people)

    def display_info(self):
        print(f'\n{ru.NAME}: {self.name}')
        print(f'{ru.MULTYPURPOSE_UNITS}: {self.resources}')
        print(f'{ru.POPULATION}: {self.people}')
        print(f'{ru.MILITARY_POWER}: {self.military}')

    def searching(self):
        self.resources -= 200
        self.people -= 10
        probability = rd.randint(1, 100)
        if 20 <= probability <= 99:
            self.resources += 350
            self.people += 10
            print(f'\n{ru.EXPEDITION_RESULT_LUCK}')
        else:
            print(f'\n{ru.EXPEDITION_RESULT_UNLUCK}')

    def upgrading(self):
        self.resources -= 20
        print(f'\n{ru.UPGRADING_CHOICE}')
        while True:
            choice = input()
            if choice in (ru.FACTORY, ru.FACTORY_2):
                self.station_factory += 1
                print(f'\n{ru.FACTORY_BUILT}')
                input()
                break
            elif choice in (ru.FARM, ru.FARM_2):
                self.station_farm += 1
                print(f'\n{ru.FARM_BUILT}')
                input()
                break
            else:
                print(ru.WRONG_CHOICE)

    def battle(self, enemy):
        self_power = 0.7 * self.military + 0.3 * self.people
        enemy_power = 0.7 * enemy.military + 0.3 * enemy.people
        winner, loser = (self, enemy) if self_power > enemy_power else (enemy, self)
        winner.resources += 20
        loser.resources -= 30
        loser.people -= 40
        print(f'\n{ru.WINNER} - {winner.name}, {ru.LOSER} - {loser.name}.')
        return winner, loser
