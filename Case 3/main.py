# Case-study 3
# Developers: Dak A., Kryukov G., Lebedev N., Cheremisina E.
#

import math as mt
import station as st
import random_events as rdev


def main():
    metro_stations = ['Площадь Карла Маркса', 'Студенческая', 'Речной вокзал',
                      'Октябрьская', 'Площаль Ленина', 'Красный проспект',
                      'Гагаринская', 'Заельцовская', 'Площадь Гарина-Михайловского',
                      'Сибирская', 'Маршала Покрышкина', 'Березовая роща', 'Золотая нива']
    names = []
    for k in range(3):
        print(f'{k + 1}-ая команда, выберите номер станции, за которую хотите играть:\n')
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
                    print('Такой станции нет, попробуйте снова.')
            except ValueError:
                print('Введите индекс станции(число).')
    st_1 = st.Station(names[0])
    st_2 = st.Station(names[1])
    st_3 = st.Station(names[2])
    enemy = st.Station('')
    names = [st_1.name, st_2.name, st_3.name]
    stations = {st_1.name: st_1, st_2.name: st_2, st_3.name: st_3}
    actions_names = ['Вылазка', 'Прокачка', 'Битва']
    actions = {'Вылазка': rdev.objst.searching, 'Прокачка': rdev.objst.upgrading, 'Битва': rdev.objst.battle}
    turn_counter = 0

    for i in range(1, 7):
        turn_counter += 1
        print('\nВведите индекс станции, которая собирается сделать ход: ')
        for i in range(3):
            print(f'{i + 1}. {names[i]}')
        while True:
            try:
                st_index_turn = int(input())
                if st_index_turn in [1, 2, 3]:
                    rdev.objst = stations[names[st_index_turn - 1]]
                    break
                else:
                    print("Такой станции нет, попробуйте снова.")
            except ValueError:
                print("Введите индекс станции(число).")
        print('\nЧто вы хотите сделать?')
        if turn_counter == 1:
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
                        rdev.random_choice_local()
                        input()
                        break
                    case 2:
                        actions.get(actions_names[1])()
                        rdev.random_choice_local()
                        input()
                        break
                    case 3:
                        print('\nВведите индекс станции, на которую хотите напасть:')
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
                        rdev.objst.battle(enemy)
                        rdev.objst.display_info()
                        enemy.display_info()
                        break
                    case _:
                        print('Такого действия нет, попробуйте снова.')
            except ValueError:
                print('Введите индекс действия(число).')

    result_list = [st_1.result, st_2.result, st_3.result]
    result_list.sort()

    result = {st_1.result: st_1, st_2.result: st_2, st_3.result: st_3}
    winner = result.get(max(result_list))
    loser = result.get(min(result_list))
    print(f'Победившая станция: {winner}')
    print(f'Проигравшая станция: {loser}')
    for i in range(2):
        result_list.pop(i)
    mid = result.get(0)
    print(f'Станция "Посередине" {mid}')
    
    
if __name__ == '__main__':
    main()
