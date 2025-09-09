# Case-study 3
# Developers: Dak A., Kryukov G., Lebedev N., Cheremisina E.
#

import station as st
import random_events as rdev
import ru_local as ru

def main():
    metro_stations = [
        ru.PLOSHCHAD_MARKSA, ru.STUDENCHESKAYA, ru.RECHNOY_VOKZAL,
        ru.OKTYABRSKAYA, ru.PLOSHCHAD_LENINA, ru.KRASNY_PROSPEKT,
        ru.GAGARINSKAYA, ru.ZAELTSOVSKAYA, ru.PLOSHCHAD_GAGARINA_MIKHAYLOVSKOGO,
        ru.SIBIRSKAYA, ru.MARSHALA_POKRYSHKINA, ru.BERYOZOVAYA_ROSCHA, ru.ZOLOTAYA_NIVA
    ]
    names = []

    for k in range(3):
        print(f'\n{k + 1}{ru.STATION_CHOICE}\n')
        for n in range(len(metro_stations)):
            print(f'{n + 1}. {metro_stations[n]}')
        while True:
            try:
                index = int(input())
                if 1 <= index <= len(metro_stations):
                    name = metro_stations.pop(index - 1)
                    names.append(name)
                    break
                else:
                    print(ru.WRONG_STATION)
            except ValueError:
                print(ru.INCORRECT_STATION)

    st_1 = st.Station(names[0])
    st_2 = st.Station(names[1])
    st_3 = st.Station(names[2])

    stations = {st_1.name: st_1, st_2.name: st_2, st_3.name: st_3}
    actions_names = [ru.EXPEDITION, ru.UPGRADING, ru.BATTLE]
    turn_counter = 0

    for i in range(1, 19):
        turn_counter += 1
        current_name = names[(i - 1) % 3]
        station = stations[current_name]

        print(f'\n{ru.STATION_TURN}{station.name}')
        station.display_info()
        print(f'\n{ru.TURN_CHOICE}')

        lim = 2 if turn_counter <= 3 else 3
        for j in range(lim):
            print(f'{j + 1}. {actions_names[j]}')

        while True:
            try:
                turn_choice = int(input())
                match turn_choice:
                    case 1:
                        station.searching()
                        input()
                        break
                    case 2:
                        station.upgrading()
                        rdev.random_choice_local(station)
                        input()
                        break
                    case 3:
                        print(f'\n{ru.BATTLE_CHOICE}')
                        enemies = [n for n in names if n != station.name]
                        for k in range(2):
                            print(f'{k + 1}. {enemies[k]}')
                        enemy_index = int(input())
                        enemy = stations.get(enemies[enemy_index - 1])
                        rdev.random_choice_battle(station)
                        input()
                        print(f'{ru.END_BATTLE}')
                        station.battle(enemy)
                        break
                    case _:
                        print(ru.WRONG_ACTION)
            except ValueError:
                print(ru.INCORRECT_ACTION)

        station.people += 10 * station.station_farm - 20
        station.military += 5 * station.station_factory - 10
        station.display_info()

    print(f'\n{ru.RESULT}')
    input()

    results = [
        (st_1.result_value(), st_1.name),
        (st_2.result_value(), st_2.name),
        (st_3.result_value(), st_3.name)
    ]
    results_sorted = sorted(results, key=lambda x: x[0])
    winner = results_sorted[2][1]
    loser = results_sorted[0][1]
    mid = results_sorted[1][1]

    print(f'{ru.END_WINNER} {winner}')
    print(f'{ru.END_LOSER} {loser}')
    print(f'{ru.END_MEDIUM} {mid}')

if __name__ == '__main__':
    main()
