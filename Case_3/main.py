# Case-study 3
# Developers: Dak A., Kryukov G., Lebedev N., Cheremisina E.
#

import math as mt
import station as st
import random_events as rdev
import ru_local as ru


def main():
    '''
    main function, describing all gaming process
    :return: None
    '''
    metro_stations = [ru.PLOSHCHAD_MARKSA, ru.STUDENCHESKAYA, 
                    ru.RECHNOY_VOKZAL, ru.OKTYABRSKAYA, ru.PLOSHCHAD_LENINA, 
                    ru.KRASNY_PROSPEKT, ru.GAGARINSKAYA, ru.ZAELTSOVSKAYA, 
                    ru.PLOSHCHAD_GAGARINA_MIKHAYLOVSKOGO, ru.SIBIRSKAYA, 
                    ru.MARSHALA_POKRYSHKINA, ru.BERYOZOVAYA_ROSCHA, 
                    ru.ZOLOTAYA_NIVA]
    names = []
    for k in range(3):
        print(f'\n{k + 1}{ru.STATION_CHOICE}\n')
        for n in range(len(metro_stations)):
            print(f'{n + 1}. {metro_stations[n]}')
        while True:
            try:
                index = int(input())
                if 1 <= index <= len(metro_stations):
                    name = metro_stations[index - 1]
                    names.append(name)
                    metro_stations.pop(index - 1)
                    break
                else:
                    print(ru.WRONG_STATION)
            except ValueError:
                print(ru.INCORRECT_STATION)

    st_1 = st.Station(names[0])
    st_2 = st.Station(names[1])
    st_3 = st.Station(names[2])
    enemy = st.Station('')
    names = [st_1.name, st_2.name, st_3.name]
    stations = {st_1.name: st_1, st_2.name: st_2, st_3.name: st_3}
    actions_names = [ru.EXPEDITION, ru.UPGRADING, ru.BATTLE]
    actions = {ru.EXPEDITION: rdev.objst.searching, 
               ru.UPGRADING: rdev.objst.upgrading, 
               ru.BATTLE: rdev.objst.battle}
    turn_counter = 0

    for i in range(1, 7):
        turn_counter += 1
        print(f'\n{ru.STATION_TURN}')
        for i in range(3):
            print(f'{i + 1}. {names[i]}')
        while True:
            try:
                st_index_turn = int(input())
                if st_index_turn in [1, 2, 3]:
                    rdev.objst = stations[names[st_index_turn - 1]]
                    break
                else:
                    print(ru.WRONG_STATION)
            except ValueError:
                print(ru.INCORRECT_STATION)
        rdev.objst.display_info()
        print(f'\n{ru.TURN_CHOICE}')
        if turn_counter <= 3:
            lim = 2
        else:
            lim = 3

        for i in range(lim):
            print(f'{i + 1}. {actions_names[i]}')
        while True:
            try:
                turn_choice = int(input())
                match turn_choice:
                    case 1:
                        actions.get(actions_names[0])()
                        input()
                        break
                    case 2:
                        actions.get(actions_names[1])()
                        rdev.random_choice_local()
                        input()
                        break
                    case 3:
                        print(f'\n{ru.BATTLE_CHOICE}')
                        enemies = [n for n in names if n != rdev.objst.name]
                        for i in range(2):
                            print(f'{i + 1}. {enemies[i]}')
                        enemy_index = int(input())
                        match enemy_index:
                            case 1:
                                enemy = stations.get(enemies[0])
                            case 2:
                                enemy = stations.get(enemies[1])
                        rdev.random_choice_battle()
                        input()
                        print(f'{ru.END_BATTLE}')
                        winner, loser = rdev.objst.battle(enemy)
                        break
                    case _:
                        print(ru.WRONG_ACTION)
            except ValueError:
                print(ru.INCORRECT_ACTION)
        rdev.objst.people += 10 * rdev.objst.station_farm - 20
        rdev.objst.military += 5 * rdev.objst.station_factory - 10
        rdev.objst.display_info()
    
    print(f'\n{ru.RESULT}')
    input()
    
    results = [
        (st_1.result, st_1.name), 
        (st_2.result, st_2.name),
        (st_3.result, st_3.name)
    ]
    results_sorted = sorted(results, key=lambda x: x[0])
    winner = results[-1][1]
    loser = results[0][1]
    mid = results[1][1]

    print(f'{ru.END_WINNER} {winner}')
    print(f'{ru.END_LOSER} {loser}')
    print(f'{ru.END_MEDIUM} {mid}')
    
    
if __name__ == '__main__':
    main()
