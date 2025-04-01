# Case-study 3
# Developers: Dak A., Kryukov G., Lebedev N., Cheremisina E.
#

import math
import station as st
import random_events as rdev

def main():
    st_1 = st.Station('Речной вокзал')
    st_2 = st.Station('Золотая нива')
    st_3 = st.Station('Заельцовская')
    names = [st_1.name, st_2.name, st_3.name]
    stations = {st_1.name: st_1, st_2.name: st_2, st_3.name: st_3}

    for i in range(1, 7):
        print('\nВведите индекс станции, которая собирается сделать ход: ')
        for i in range(3):
            print(f'{i + 1}. {names[i]}')
        while True:
            try:
                st_index_turn = int(input())
                match st_index_turn:
                    case 1:
                        rdev.objst = st_1
                        rdev.objst.display_info()
                        break
                    case 2:
                        rdev.objst = st_2
                        rdev.objst.display_info()
                        break
                    case 3:
                        rdev.objst = st_3
                        rdev.objst.display_info()
                        break
                    case _:
                        print("Такой станции нет, попробуйте снова.")
            except ValueError:
                print("Введите индекс станции(число).")
        print('\nЧто вы хотите сделать?')
        print('1. Вылазка', '2. Прокачка станции', '3. Битва')
        while True:
            try:
                turn_choice = int(input())
                match turn_choice:
                    case 1:
                        rdev.objst.searching()
                        rdev.random_choice_local()
                    case 2:
                        rdev.objst.upgrading()
                        rdev.random_choice_local()
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
                        names.append(rdev.objst.name)
                        rdev.random_choice_battle()
                        input()
                        rdev.objst.battle(enemy)
                        rdev.objst.display_info()
                        enemy.display_info()
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
