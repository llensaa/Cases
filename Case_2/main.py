# Part of case-study #2: Colonization of Mars
# Developers: Dak A., Kruykov G., Lebedev N., Cheremisina E.
#

import ru_local as ru

def main():
    '''
    Main function.
    :return: None
    '''
    
    people = int(input(ru.PEOPLE_NUM))
    length = int(input(ru.MISSION_LENGTH))
    water_per_person = 2.2
    oxygen_per_person = 0.84
    food_per_person = 1.6
    electricity_per_person = 5
    safety_reserve = 0.1

    water_quantity = water_per_person * people * length
    oxygen_quantity = oxygen_per_person * people * length
    food_quantity = food_per_person * people * length
    electricity_quantity = electricity_per_person * 24 * people * length

    total_water *= (1 + safety_reserve)
    total_oxygen *= (1 + safety_reserve)
    total_food *= (1 + safety_reserve)
    total_energy *= (1 + safety_reserve)

    print(f'{ru.WATER_REQUIRED} - {"{:.1f}".format(water_quantity)} {ru.LITRES}')
    print(f'{ru.OXYGEN_REQUIRED} - {"{:.1f}".format(oxygen_quantity)} {ru.KG}')
    print(f'{ru.FOOD_REQUIRED} - {"{:.1f}".format(food_quantity)} {ru.KG}')
    print(f'{ru.ELECTRICITY_REQUIRED} - {"{:.1f}".format(electricity_quantity)} {ru.KILOWATT}')

    print(f'{ru.SAFETY_RESERVE}')
    print(f'{"{:.1f}".format(total_water)} {ru.LITRES}')
    print(f'{"{:.1f}".format(total_oxygen)} {ru.KG}')
    print(f'{"{:.1f}".format(total_food)} {ru.KG}')
    print(f'{"{:.1f}".format(total_energy)} {ru.KILOWATT}')

if __name__ == '__main__':
    main()
