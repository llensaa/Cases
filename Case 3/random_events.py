import random as rd
import station as st
import ru_local as ru

objst = st.Station('')

def random_choice_local():
    event = rd.randint(1, 17)
    number_resources = rd.randint(1,5)
    number_military = rd.randint(1, 4)
    number_people = rd.randint(1, 3)

    match event:
        case 1:
            print(f'\n{ru.DOWNFALL}')
            objst.resources -= 100
            objst.people -= 15
        case 2:
            print(f'\n{ru.BUILDING_MATERIALS}')
            objst.resources += 50 * number_resources
        case 3:
            print(f'\n{ru.ARMAMENT}')
            objst.military += 15 * number_military
        case 4:
            print(f'\n{ru.MUTANT_ATTACK}')
            objst.people -= 15
            objst.military -= 5 * number_military
        case 5:
            print(f'\n{ru.REBEL}')
            objst.people -= 30
            objst.military -= 5 * number_military
        case 6:
            print(f'\n{ru.OUTER_RESIDENTS}')
            objst.people += 10 * number_people
        case 7:
            print(f'\n{ru.BANDITS_ATTACK}')
            objst.military -= 5 * number_military
        case 8:
            print(f'\n{ru.FLOOD}')
            objst.people -= 5 * number_people
            objst.military -= 2 * number_military
        case 9:
            print(f'\n{ru.KNIFING}')
            objst.people -= 2 * number_people
            objst.military -= number_military
        case 10:
            print(f'\n{ru.DESERTER}')
            objst.people -= 2 * number_people
            objst.military -= 3 * number_military
        case 11:
            print(f'\n{ru.EPIDEMY}')
            objst.people -= 4 * number_people
            objst.military -= number_military
        case 12:
            print(f'\n{ru.LEAN_YEAR}')
            objst.people -= 8 * number_people
            objst.military -= 4 * number_military
        case 13:
            print(f'\n{ru.UNFAMILIAR_ROOM}')
            objst.resources += 100
            objst.military += 5 * number_military
        case 14:
            print(f'\n{ru.STRANGE_SIGNAL}')
        case 15:
            print(f'\n{ru.MISSING_SQUAD}')
            objst.people -= 10
            objst.military -= 5 * number_military
        case 16:
            print(f'\n{ru.PEOPLE_GOOD_INTENTIONS}')
            objst.people += 4 * number_people
            objst.military += 5 * number_military
        case 17:
            print(f'\n{ru.WEEPING}')
            objst.people -= 2 * number_people

def random_choice_battle():
    event_2 = rd.randint(18, 25)
    number_resources = rd.randint(1,5)
    number_military = rd.randint(1, 4)
    number_people = rd.randint(1, 3)
    match event_2:
        case 18:
            print(f'\n{ru.DOWNFALL_BATTLE}')
            objst.resources -= 100
            objst.people -= 15
        case 19:
            print(f'\n{ru.TROPHY_ARMAMENT}')
            objst.military += 15
        case 20:
            print(f'\n{ru.IRRADIATION}')
            objst.military -= 5 * number_military
            objst.people -= 10
        case 21:
            print(f'\n{ru.ANOMALY}')
            objst.people -= 10
        case 22:
            print(f'\n{ru.MUTANT_ATTACK_BATTLE}')
            objst.military -= 5 * number_military
            objst.people -= 10
        case 23:
            print(f'\n{ru.ARMORED_TRAIN}')
            objst.military += 25
        case 24:
            print(f'\n{ru.CRATES_OF_SUPPLIES}')
            objst.resources += 10 * number_resources
        case 25:
            print(f'\n{ru.HIDDEN_SETTLEMENT}')
            objst.people += 20 * number_people
