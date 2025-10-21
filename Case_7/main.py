import turtle as trt


def get_num_hexagons() -> int:
    while True:
        try:
            num = int(input('Пожалуйста, введите желаемое количество шестиугольников: '))
            if num in [i for i in range(4, 21)]:
                break
            print('Оно должно быть от 4 до 20.')
        except ValueError:
            print('Введите число')
    return num


def color_choice() -> dict:
    colors = {'Белый': 'white', 'Красный': 'red', 'Фиолетовый': 'purple',
              'Жёлтый': 'yellow', 'Чёрный': 'black', 'Оранжевый': 'orange'}
    chosen_colors = {}
    for i in range(2):
        print('Допустимые цвета заливки')
        for j in colors.keys():
            print(j)
        while True:
            chosen_color = input('Выберите желаемый цвет заливки: ')
            if chosen_color in colors:
                chosen_colors[chosen_color] = colors.get(chosen_color)
                del colors[chosen_color]
                break
            print(f'\'{chosen_color}\' не является верным значением')

    return chosen_colors


def draw_hexagon(x, y, side_len, color):
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
    counter_i = 0
    counter_j = 0

    colors = color_choice()
    used_colors = colors.values()
    colors_list = [a for a in used_colors]
    color1 = colors_list[0]
    color2 = colors_list[1]

    num = get_num_hexagons()
    x0 = 0
    y0 = 0
    hex_height = 500 // num
    hex_side_len = hex_height / (3 ** 0.5)
    for i in range(num):
        counter_i += 1
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
            x0 = -hex_height / 2
        else:
            x0 = 0
        y0 -= hex_height / (2 * 3 ** 0.5) + hex_side_len


draw_tesselation()

trt.done()
