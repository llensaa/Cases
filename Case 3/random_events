import random as rd
import station as st

objst = st.Station('Моя станция')
event = rd.randint(1, 20)
number_resources = rd.randint(1,5)
number_militaty = rd.randint(1, 4)
number_people = rd.randint(1, 3)
match event:
    case 1:
        print('Произошёл обвал на станции!')
        objst.resources -= 100
        objst.people -= 15
    case 2:
        print('Ваши люди нашли запасы строительных материалов')
        objst.resources += 50 * number_resources
    case 3:
        print('В близлежащем тоннеле были обнаружены'
              ' оружие и обмундирование')
        objst.military += 15 * number_militaty
    case 4:
        print('На станцию напали мутанты!')
        objst.people -= 15
        objst.military -= 5 * number_militaty
    case 5:
        print('На станции произошёл бунт!')
        objst.people -= 30
        objst.military -= 5 * number_militaty
    case 6:
        print('К вам присоединились жители с ближайших тоннелей')
        objst.people += 10 * number_people
    case 7:
        print('На станцию напали бандиты!')
        objst.military -= 5 * number_militaty
    case 8:
        print('Станцию затопило!')
        objst.people -= 5 * number_people
        objst.military -= 2 * number_militaty
    case 9:
        print('На станции произошла поножовщина!')
        objst.people -= 2 * number_people
        objst.military -= number_military
    case 10:
        print('Отряд военных дезертировал и забрал с собой оружие!')
        objst.people -= 2 * number_people
        objst.military -= 3 * number_military
    case 11:
        print('На станции началась эпидемия!')
        objst.people -= 4 * number_people
        objst.military -= number_military
    case 12:
        print('Этот год неурожайный, провианта на всех не хватает!')
        objst.people -= 8 * number_people
        objst.military -= 4 * number_military
    case 13:
        print('Вы нашли ранее неизвестную комнату'
              ' на станции, в которой оказались большие запасы ресурсов!')
        objst.resources += 100
        objst.military += 5 * number_military
    case 14:
        print('Ваша радиостанция уловила странный сигнал!'
              ' Значит ли это, что не только Вы остались в живых?...')
    case 15:
        print('Отряд военных отправился на поиски ресурсов'
              ' в тоннель, однако спустя 3 дня они так и не вернулись.')
        objst.people -= 10
        objst.military -= 5 * number_military
    case 16:
        print('На вашу станцию пришли люди с оружием, но'
              ' злых намерений у них нет, им просто нужно убежище.')
        objst.people += 4 * number_people
        objst.military += 5 * number_military
    case 17:
        print('Уже вторую неделю из тоннелей раздается плач'
              ' ребенка. Все, кто пытался узнать, что является'
              ' источником звука, так и не вернулись на станцию.')
        objst.people -= 2 * number_people
