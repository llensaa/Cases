import random as rd
import station as st

obj = st.Station('Моя станция')
event = rd.randint(1, 20)
number_resources = rd.randint(1,5)
number_militaty = rd.randint(1, 4)
number_people = rd.randint(1, 3)
match event:
    case 1:
        print('Произошёл обвал на станции!')
        obj.resources -= 100
        obj.people -= 15
    case 2:
        print('Ваши люди нашли запасы строительных материалов')
        obj.resources += 50 * number_resources
    case 3:
        print('В близдежащем тоннелле были обнаружены'
              ' оружие и обмундирование')
        obj.military += 15 * number_militaty
    case 4:
        print('На станцию напали мутанты!')
        obj.people -= 15
        obj.military -= 5 * number_militaty
    case 5:
        print('На станции произошёл бунт!')
        obj.people -= 30
        obj.military -= 5 * number_militaty
    case 6:
        print('К вам присоединились жители с ближайших тоннелей')
        obj.people += 10 * number_people
    case 7:
        print('На станцию напали бандиты!')
        obj.military -= 5 * number_militaty
    case 8:
        print('Станцию затопило!')
        obj.people -= 5 * number_people
        obj.military -= 2 * number_militaty
