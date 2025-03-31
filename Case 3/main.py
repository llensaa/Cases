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
    st_1.display_info()
    st_2.display_info()
    st_3.display_info()

    for i in range(1, 7):
        st_1.display_info()
        st_2.display_info()
        st_3.display_info()

        print('Введите индекс станции, которая собирается сделать ход: ')
        for i in range(3):
            print(f'{i + 1}. {names[i]}')
        st_index_turn = int(input())
        match st_index_turn:
            case 1:
                rdev.objst = st_1
            case 2:
                rdev.objst = st_2
            case 3:
                rdev.objst = st_3
        print('Что вы хотите сделать?')
        print('1. Вылазка', '2. Прокачка станции', '3. Битва')
        turn_choice = int(input())
        match turn_choice:
            case 1:
                rdev.objst.searching()
            case 2:
                rdev.objst.upgrading()
            case 3:
                print('Введите индекс станции, на которую хотите напасть:')
                enemies = [n for n in names if n != rdev.objst.name]
                for i in range(2):
                    print(f'{i + 1}. {names[i]}')
                enemy_index = int(input())
                match enemy_index:
                    case 1:
                        enemy = stations.get(names[0])
                    case 2:
                        enemy = stations.get(names[1])
                names.append(rdev.objst.name)
                rdev.objst.battle(enemy)
        
        rdev.objst.random_choice()    
    

if __name__ == '__main__':
    main()
