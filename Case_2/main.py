# Part of case-study #2: Colonization of Mars
# Developers:
#

import ru_local as ru

def main():
    '''
    Main function.
    :return: None
    '''

    people = int(input(ru.PEOPLE_NUM))
    length = int(input(ru.MISSION_LENGTH))
    water_per_person = 3
    oxygen_per_person = 0.84
    food_per_person = 2
    electricity_per_person = 5

    water_quantity = water_per_person * people * length
    oxygen_quantity = oxygen_per_person * people * length
    food_quantity = food_per_person * people * length
    electricity_quantity = electricity_per_person * 24 * people * length

    print(f'{ru.WATER_REQUIRED} - {water_quantity} {ru.LITRES}')
    print(f'{ru.OXYGEN_REQUIRED} - {oxygen_quantity} {ru.KG}')
    print(f'{ru.FOOD_REQUIRED} - {food_quantity} {ru.KG}')
    print(f'{ru.ELECTRICITY_REQUIRED} - {electricity_quantity} {ru.KILOWATT}')


if __name__ == '__main__':
    main()
