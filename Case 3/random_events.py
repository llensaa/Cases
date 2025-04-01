import random as rd
import station as st

objst = st.Station('Моя станция')
event = rd.randint(1, 17)
event_2 = rd.randint(18, 25)
number_resources = rd.randint(1,5)
number_military = rd.randint(1, 4)
number_people = rd.randint(1, 3)

def random_choice_local():
    match event:
        case 1:
            print('\nПроизошёл обвал на станции!')
            objst.resources -= 100
            objst.people -= 15
        case 2:
            print('\nВаши люди нашли запасы строительных материалов')
            objst.resources += 50 * number_resources
        case 3:
            print('\nВ близлежащем тоннеле были обнаружены'
                ' оружие и обмундирование')
            objst.military += 15 * number_military
        case 4:
            print('\nНа станцию напали мутанты!')
            objst.people -= 15
            objst.military -= 5 * number_military
        case 5:
            print('\nНа станции произошёл бунт!')
            objst.people -= 30
            objst.military -= 5 * number_military
        case 6:
            print('\nК вам присоединились жители с ближайших тоннелей')
            objst.people += 10 * number_people
        case 7:
            print('\nНа станцию напали бандиты!')
            objst.military -= 5 * number_military
        case 8:
            print('\nСтанцию затопило!')
            objst.people -= 5 * number_people
            objst.military -= 2 * number_military
        case 9:
            print('\nНа станции произошла поножовщина!')
            objst.people -= 2 * number_people
            objst.military -= number_military
        case 10:
            print('\nОтряд военных дезертировал и забрал с собой оружие!')
            objst.people -= 2 * number_people
            objst.military -= 3 * number_military
        case 11:
            print('\nНа станции началась эпидемия!')
            objst.people -= 4 * number_people
            objst.military -= number_military
        case 12:
            print('\nЭтот год неурожайный, провианта на всех не хватает!')
            objst.people -= 8 * number_people
            objst.military -= 4 * number_military
        case 13:
            print('\nВы нашли ранее неизвестную комнату'
                ' на станции, в которой оказались большие запасы ресурсов!')
            objst.resources += 100
            objst.military += 5 * number_military
        case 14:
            print('\nВаша радиостанция уловила странный сигнал!'
                ' Значит ли это, что не только Вы остались в живых?...')
        case 15:
            print('\nОтряд военных отправился на поиски ресурсов'
                ' в тоннель, однако спустя 3 дня они так и не вернулись.')
            objst.people -= 10
            objst.military -= 5 * number_military
        case 16:
            print('\nНа вашу станцию пришли люди с оружием, но'
                ' злых намерений у них нет, им просто нужно убежище.')
            objst.people += 4 * number_people
            objst.military += 5 * number_military
        case 17:
            print('\nУже вторую неделю из тоннелей раздается плач'
                ' ребенка. Все, кто пытался узнать, что является'
                ' источником звука, так и не вернулись на станцию.')
            objst.people -= 2 * number_people

def random_choice_battle():
    match event_2:
        case 18:
            print('\nПроизошёл обвал в тоннеле')
            objst.resources -= 100
            objst.people -= 15
        case 19:
            print('\nПо пути на битву вы получили'
                  ' боеприпасы и оружие')
            objst.military += 15
        case 20:
            print('\nВаши бойцы получили сильное облучение'
                  ' и часть из них теперь не боеспособна')
            objst.military -= 5 * number_military
            objst.people -= 10
        case 21:
            print('\nКогда ваши люди возвращались с битвы,'
                  ' они наткнулись на аномалию.'
                  ' Лишь часть из них вернулась в живых')
            objst.people -= 10
        case 22:
            print('\nВ момент атаки на ваших людей напала стая мутантов')
            objst.military -= 5 * number_military
            objst.people -= 10
        case 23:
            print('\nВ тоннелях метро вы нашли брошенный бронепоезд,'
                  ' чей же он может быть?')
            objst.military += 25
        case 24:
            print('\nВы обнаружили ящики с припасами на базе бандитов')
            objst.resources += 10 * number_resources
        case 25:
            print('\nВозвращаясь с миссии вы обнаружили скрытое поселение,'
                  ' его люди присоединяются к вам')
            objst.people += 20 * number_people
