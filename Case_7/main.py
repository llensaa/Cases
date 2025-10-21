import turtle as trt


def draw_hexagon(x, y, side_len, color):
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
    pass


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
    colors = {'c1': 't1', 'c2': 't2', 'c3': 't3', 'c4': 't4', 'c5': 't5', 'c6': 't6'}
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


def draw_tessellation(num):
    colors_dict = color_choice()
    for i in range(get_num_hexagons()):
        for j in
