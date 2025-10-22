import turtle as trt
import random
import ru_local as ru


def get_num_hexagons() -> int:
    '''
    function, returning number of hexagons in row user entered
    :return: num
    '''
    while True:
        try:
            num = int(input(ru.ENTER_HEXAGONS))
            if num in [i for i in range(4, 21)]:
                break
            print(ru.MUST_BE_4_TO_20)
        except ValueError:
            print(ru.ENTER_NUMBER)
    return num


def color_choice() -> dict:
    '''
    function, returning dict with colors user chose
    :return: chosen_colors
    '''
    colors = {'Белый': 'white', 'Красный': 'red', 'Фиолетовый': 'purple',
              'Жёлтый': 'yellow', 'Чёрный': 'black', 'Оранжевый': 'orange',
              'Синий': 'blue', 'Зелёный': 'green', 'Розовый': 'pink',
              'Коричневый': 'brown', 'Серый': 'gray', 'Голубой': 'cyan'}

    while True:
        choice = input(ru.CHOOSE_MODE)
        if choice == '1':
            color_names = random.sample(list(colors.keys()), 2)
            chosen_colors = {}
            for color_name in color_names:
                chosen_colors[color_name] = colors[color_name]

            print(f'{ru.RANDOM_CHOSEN} {", ".join(color_names)}')
            return chosen_colors

        elif choice == '2':
            chosen_colors = {}

            for i in range(2):
                print('_' * 50)
                print('\n' + ru.AVAILABLE_COLORS + '\n')
                color_list = list(colors.keys())
                for idx in range(0, len(color_list), 2):
                    line = ""
                    for j in range(2):
                        if idx + j < len(color_list):
                            color_name = color_list[idx + j]
                            padded_color = color_name.ljust(15)
                            line += padded_color
                    print(line)
                print('_' * 50)

                while True:
                    chosen_color = input(f'{ru.CHOOSE} {i + 1}{ru.FILL_COLOR}')
                    if chosen_color in colors:
                        chosen_colors[chosen_color] = colors[chosen_color]
                        del colors[chosen_color]
                        break
                    print(f'\'{chosen_color}\' {ru.INVALID_VALUE}')

            return chosen_colors

        else:
            print(ru.ENTER_1_OR_2)


def draw_hexagon(x, y, side_len, color):
    '''
    function, drawing hexagon
    :param x: x coordinate
    :param y: y coordinate
    :param side_len: length of hexagons side
    :param color: hexagons fillcolor
    :return: None
    '''
    trt.tracer(0)
    trt.right(90)
    trt.fillcolor(color)
    trt.setpos(x, y)
    trt.pendown()
    trt.begin_fill()
    for _ in range(6):
        trt.forward(side_len)
        trt.left(60)
    trt.end_fill()
    trt.penup()
    trt.home()


def draw_tesselation():
    '''
    function, drawing tesselation
    :return: None
    '''
    colors = color_choice()
    used_colors = colors.values()

    colors_list = [a for a in used_colors]
    color1, color2 = colors_list[0], colors_list[1]

    num = get_num_hexagons()
    x0 = -250
    y0 = 250
    hex_height = 500 // num
    hex_side_len = hex_height / (3 ** 0.5)
    for i in range(num):
        for j in range(num):
            if (i // 2) % 2:
                if j % 2:
                    color = color1
                else:
                    color = color2
            else:
                if j % 2:
                    color = color2
                else:
                    color = color1
            draw_hexagon(x0, y0, hex_side_len, color)
            x0 += hex_height
        if not i % 2:
            x0 = - 250 - hex_height / 2
        else:
            x0 = -250
        y0 -= hex_height / (2 * 3 ** 0.5) + hex_side_len
    print(ru.DRAW)


draw_tesselation()

trt.done()
