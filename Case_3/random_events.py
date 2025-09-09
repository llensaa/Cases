import random as rd
import ru_local as ru

def random_choice_local(station):
    event = rd.randint(1, 17)
    r = rd.randint(1, 5)
    m = rd.randint(1, 4)
    p = rd.randint(1, 3)

    match event:
        case 1:
            print(f'\n{ru.DOWNFALL}')
            station.resources -= 100
            station.people -= 15
        case 2:
            print(f'\n{ru.BUILDING_MATERIALS}')
            station.resources += 50 * r
        case 3:
            print(f'\n{ru.ARMAMENT}')
            station.military += 15 * m
        case 4:
            print(f'\n{ru.MUTANT_ATTACK}')
            station.people -= 15
            station.military -= 5 * m
        case 5:
            print(f'\n{ru.REBEL}')
            station.people -= 30
            station.military -= 5 * m
        case 6:
            print(f'\n{ru.OUTER_RESIDENTS}')
            station.people += 10 * p
        case 7:
            print(f'\n{ru.BANDITS_ATTACK}')
            station.military -= 5 * m
        case 8:
            print(f'\n{ru.FLOOD}')
            station.people -= 5 * p
            station.military -= 2 * m
        case 9:
            print(f'\n{ru.KNIFING}')
            station.people -= 2 * p
            station.military -= m
        case 10:
            print(f'\n{ru.DESERTER}')
            station.people -= 2 * p
            station.military -= 3 * m
        case 11:
            print(f'\n{ru.EPIDEMY}')
            station.people -= 4 * p
            station.military -= m
        case 12:
            print(f'\n{ru.LEAN_YEAR}')
            station.people -= 8 * p
            station.military -= 4 * m
        case 13:
            print(f'\n{ru.UNFAMILIAR_ROOM}')
            station.resources += 100
            station.military += 5 * m
        case 14:
            print(f'\n{ru.STRANGE_SIGNAL}')
        case 15:
            print(f'\n{ru.MISSING_SQUAD}')
            station.people -= 10
            station.military -= 5 * m
        case 16:
            print(f'\n{ru.PEOPLE_GOOD_INTENTIONS}')
            station.people += 4 * p
            station.military += 5 * m
        case 17:
            print(f'\n{ru.WEEPING}')
            station.people -= 2 * p

def random_choice_battle(station):
    event = rd.randint(18, 25)
    r = rd.randint(1, 5)
    m = rd.randint(1, 4)
    p = rd.randint(1, 3)

    match event:
        case 18:
            print(f'\n{ru.DOWNFALL_BATTLE}')
            station.resources -= 100
            station.people -= 15
        case 19:
            print(f'\n{ru.TROPHY_ARMAMENT}')
            station.military += 15
        case 20:
            print(f'\n{ru.IRRADIATION}')
            station.military -= 5 * m
            station.people -= 10
        case 21:
            print(f'\n{ru.ANOMALY}')
            station.people -= 10
        case 22:
            print(f'\n{ru.MUTANT_ATTACK_BATTLE}')
            station.military -= 5 * m
            station.people -= 10
        case 23:
            print(f'\n{ru.ARMORED_TRAIN}')
            station.military += 25
        case 24:
            print(f'\n{ru.CRATES_OF_SUPPLIES}')
            station.resources += 10 * r
        case 25:
            print(f'\n{ru.HIDDEN_SETTLEMENT}')
            station.people += 20 * p
