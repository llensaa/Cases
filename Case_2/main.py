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
    WATER_PER_PERSON = 2.2
    OXYGEN_PER_PERSON = 0.84
    FOOD_PER_PERSON = 1.6
    ELECTRICITY_PER_PERSON = 5
    SAFETY_RESERVE = 0.1

    water_quantity = WATER_PER_PERSON * people * length
    oxygen_quantity = OXYGEN_PER_PERSON * people * length
    food_quantity = FOOD_PER_PERSON * people * length
    electricity_quantity = ELECTRICITY_PER_PERSON * 24 * people * length

    total_water = water_quantity * (1 + SAFETY_RESERVE)
    total_oxygen = oxygen_quantity * (1 + SAFETY_RESERVE)
    total_food = food_quantity * (1 + SAFETY_RESERVE)
    total_energy = electricity_quantity * (1 + SAFETY_RESERVE)

    print(f'{ru.WATER_REQUIRED} - {"{:.1f}".format(water_quantity)} {ru.LITRES}')
    print(f'{ru.OXYGEN_REQUIRED} - {"{:.1f}".format(oxygen_quantity)} {ru.KG}')
    print(f'{ru.FOOD_REQUIRED} - {"{:.1f}".format(food_quantity)} {ru.KG}')
    print(f'{ru.ELECTRICITY_REQUIRED} - {"{:.1f}".format(electricity_quantity)} {ru.KILOWATT}')

    print(f'\n{ru.SAFETY_RESERVE}')
    print(f'{"{:.1f}".format(total_water)} {ru.LITRES} {ru.WATER}')
    print(f'{"{:.1f}".format(total_oxygen)} {ru.KG} {ru.OXYGEN}')
    print(f'{"{:.1f}".format(total_food)} {ru.KG} {ru.FOOD}')
    print(f'{"{:.1f}".format(total_energy)} {ru.KILOWATT} {ru.ELECTRICITY}')


if __name__ == '__main__':
    main()
