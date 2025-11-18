import turtle as trt
import ru_local as ru


def create_l_system(iters: int, axiom: str, rules: dict) -> str:
    """
    function, initiating drawing rules for every iteration
    :param iters: number of iterations
    :param axiom: base axiom
    :param rules: base replacement
    :return:
    """
    start_str = axiom
    if not iters:
        return axiom
    end_str = ''

    for _ in range(iters):
        end_str = ''.join(rules[i] if i in rules else i for i in start_str)
        start_str = end_str

    return end_str


def draw_l_system(t, instructions: str, angle, dist: int):
    """
    function, commanding to turtle how to draw
    :param t: users turtle object
    :param instructions: L-system commands
    :param angle: turning angle
    :param dist: length of trajectory
    :return: None
    """
    for cmd in instructions:
        match cmd:
            case 'F':
                t.fd(dist)
            case '+':
                t.left(angle)
            case '-':
                t.right(angle)


def draw_fractal(iterations: int,
                 axiom: str,
                 rules: dict,
                 angle: int,
                 length=8,
                 size=2,
                 y=0,
                 x=500,
                 offset=0,
                 w=450,
                 h=450):
    """
    function, generating an L-system string using the provided axiom
    and rules, then interprets the string as turtle commands to draw
    the corresponding fractal.

    Args:
        iterations: Number of iterations to apply the L-system rules.
        axiom: The initial string (starting axiom) of the L-system.
        rules: A dictionary mapping characters to replacement strings
               according to L-system rules.
        angle: Turning angle in degrees for '+' and '-' commands.
        length: Length of each movement forward (default is 8).
        size: Scale factor for the drawing.
        y: Initial y-coordinate of the turtle (default 0).
        x: Initial x-coordinate of the turtle (default 500).
        offset: Initial heading angle of the turtle (default 0).
        w: Width of the turtle screen (default 450).
        h: Height of the turtle screen (default 450).

    Returns:
        None: The function draws directly using the turtle graphics window.
    """

    inst = create_l_system(iterations, axiom, rules)

    t = trt.Turtle()
    wn = trt.Screen()
    wn.setup(w, h)
    trt.tracer(False)

    t.penup()
    t.setx(x)
    t.sety(y)
    t.setheading(offset)
    t.pendown()

    draw_l_system(t, inst, angle, length)
    t.hideturtle()


def dragon(iterations: int, angle=90):
    """
    function, drawing Harter's dragon
    :param iterations: number of iterations
    :param angle: turning angle
    :return: None
    """
    dr_axiom = 'FX'
    dr_rules = {'X': 'X+YF+', 'Y': '-FX-Y'}
    draw_fractal(iterations, dr_axiom, dr_rules, angle, x=-100)


def levi(iterations: int, angle=45):
    """
    function, drawing Levi curve
    :param iterations: number of iterations
    :param angle: turning angle
    :return: None
    """
    levi_axiom = 'F'
    levi_rules = {'F': '-F++F-'}
    draw_fractal(iterations, levi_axiom, levi_rules, angle, x=-200)


def ice_fract_2(rec_num: int, size: float) -> None:
    """
    function drawing recursion from rec_num = number of recursions
    and size
    :param rec_num:
    :param size:
    :return: ice fract
    """
    if rec_num == 0:
        trt.forward(size)

    else:
        ice_fract_2(rec_num - 1, size / 2)
        trt.left(120)
        ice_fract_2(rec_num - 1, size / 4)
        trt.right(180)
        ice_fract_2(rec_num - 1, size / 4)
        trt.left(120)
        ice_fract_2(rec_num - 1, size / 4)
        trt.right(180)
        ice_fract_2(rec_num - 1, size / 4)
        trt.left(120)
        ice_fract_2(rec_num - 1, size / 2)


def koch_triangle(order: int, size: float) -> None:
    """
    function drawing recursive function of koch
    :param order: number of recursions
    :param size: size of figure
    :return: None
    """
    if order == 0:
        trt.forward(size)
    else:
        koch_triangle(order - 1, size / 3)
        trt.left(60)
        koch_triangle(order - 1, size / 3)
        trt.right(120)
        koch_triangle(order - 1, size / 3)
        trt.left(60)
        koch_triangle(order - 1, size / 3)


def square(size):
    for _ in range(4):
        trt.forward(size)
        trt.right(90)


def running_square(size, angle, k, depth):
    if depth == 0:
        return

    square(size)

    trt.right(angle)

    trt.penup()
    trt.forward(size * k)
    trt.pendown()

    running_square(size * (1 - k), angle, k, depth - 1)


def mink_curve(rec_num: int, size: float) -> None:
    """
    function drawing recursion from rec_num = number of recursions
    and size
    :param rec_num:
    :param size:
    :return: None
    """
    if rec_num == 0:
        trt.forward(size)
    else:
        mink_curve(rec_num - 1, size / 4)
        trt.left(90)
        mink_curve(rec_num - 1, size / 4)
        trt.right(90)
        mink_curve(rec_num - 1, size / 4)
        trt.right(90)
        mink_curve(rec_num - 1, size / 4)
        mink_curve(rec_num - 1, size / 4)
        trt.left(90)
        mink_curve(rec_num - 1, size / 4)
        trt.left(90)
        mink_curve(rec_num - 1, size / 4)
        trt.right(90)
        mink_curve(rec_num - 1, size / 4)


def tangle_6(rec: int, size: float) -> None:
    """
    Draws a recursive six-sided fractal line (hexagonal tangle).

    Args:
        rec: Current recursion depth.
        size: Length of the current segment.

    Returns:
        None: The function draws directly using the turtle graphics.
    """
    if rec == 0:
        trt.forward(size)
    else:
        tangle_6(rec - 1, size / 3)
        trt.right(120)
        for _ in range(5):
            tangle_6(rec - 1, size / 3)
            trt.left(60)
        trt.right(180)
        tangle_6(rec - 1, size / 3)


def ice_fract_1(rec_num: int, size: float) -> None:
    """
    function drawing recursion from rec_num = number of recursions
    and size
    :param rec_num:
    :param size:
    :return: ice fract
    """
    if rec_num == 0:
        trt.forward(size / 2)
        trt.left(90)
        trt.forward(size / 3)
        trt.back(size / 3)
        trt.right(90)
        trt.forward(size / 2)

    else:
        ice_fract_1(rec_num - 1, size / 4)
        trt.left(90)
        ice_fract_1(rec_num - 1, size / 6)
        trt.right(180)
        ice_fract_1(rec_num - 1, size / 6)
        trt.left(90)
        ice_fract_1(rec_num - 1, size / 4)


def sierpinski(size, depth):
    """
    function drawing sierpinski triangle
    :param size:
    :param depth: depth of recursion
    :return: drawn triangle
    """
    if depth == 0:
        for _ in range(3):
            trt.forward(size)
            trt.left(120)
    else:

        sierpinski(size / 2, depth - 1)

        trt.forward(size / 2)
        sierpinski(size / 2, depth - 1)
        trt.backward(size / 2)

        trt.left(60)
        trt.forward(size / 2)
        trt.right(60)

        sierpinski(size / 2, depth - 1)

        trt.left(60)
        trt.backward(size / 2)
        trt.right(60)

def flower(x, y):
    """
    function drawing a flower
    :param x: x-coordinate of the flower center
    :param y: y-coordinate of the flower center
    :return: None, draws directly using the turtle graphics
    """
    trt.setheading(55)
    for _ in range(4):
        trt.penup()
        trt.goto(x, y)
        trt.right(90)
        trt.forward(3)
        trt.pendown()
        trt.circle(3)

    trt.penup()
    trt.goto(x, y + 2)
    trt.pendown()
    trt.fillcolor("#CB1A1A")
    trt.begin_fill()
    trt.setheading(315)
    for _ in range(4):
        trt.forward(3)
        trt.right(90)
    trt.end_fill()



def fractal_tree(length: float, depth: int, angle: float = 28) -> None:
    """
    function drawing a deterministic fractal tree with a flower on the end of each branch
    :param length: length of the current branch
    :param depth: remaining depth of recursion
    :param angle: branching angle in degrees (default 28)
    :return: None, draws directly using the turtle graphics
    """
    if depth == 0 or length < 8:
        pos = trt.position()
        heading = trt.heading()
        flower(pos[0], pos[1])
        trt.penup()
        trt.goto(pos)
        trt.setheading(heading)
        trt.pendown()
        return

    trt.forward(length)

    pos = trt.position()
    heading = trt.heading()
    flower(pos[0], pos[1])

    trt.penup()
    trt.goto(pos)
    trt.setheading(heading)
    trt.pendown()
    trt.left(angle)
    fractal_tree(length * 0.7, depth - 1, angle)
    trt.right(2 * angle)
    fractal_tree(length * 0.7, depth - 1, angle)
    trt.left(angle)
    trt.backward(length)

def get_color_choice():
    """
    function for color selection
    """
    print("\n┌─────────────────────────────────────────────┐")
    print(f"│ {ru.COLOR_CHOICE}")
    print("├─────────────────────────────────────────────┤")
    print(f"│ {ru.COLOR_METHOD_1}")
    print(f"│ {ru.COLOR_METHOD_2}")
    print("└─────────────────────────────────────────────┘")

    color_method = input(f"\n{ru.CHOOSE_COLOR_METHOD}")

    while color_method not in ("1", "2"):
        print(ru.INVALID_COLOR)
        color_method = input(f"{ru.CHOOSE_COLOR_METHOD}").strip()

    match color_method:
        case "1":
            color_map = {
                ru.BLACK_RU: "black",
                ru.BLACK_RU_ALT: "black",
                "black": "black",
                ru.WHITE_RU: "white",
                "white": "white",
                ru.RED_RU: "red",
                "red": "red",
                ru.GREEN_RU: "green",
                "green": "green",
                ru.BLUE_RU: "blue",
                "blue": "blue",
                ru.YELLOW_RU: "yellow",
                ru.YELLOW_RU_ALT: "yellow",
                "yellow": "yellow",
                ru.ORANGE_RU: "orange",
                "orange": "orange",
                ru.PURPLE_RU: "purple",
                "purple": "purple",
                ru.PINK_RU: "pink",
                "pink": "pink",
                ru.BROWN_RU: "brown",
                "brown": "brown",
                ru.GRAY_RU: "gray",
                "gray": "gray",
                ru.CYAN_RU: "cyan",
                "cyan": "cyan",
                ru.MAGENTA_RU: "magenta",
                "magenta": "magenta"
            }
            color_input = input(f"{ru.ENTER_COLOR_NAME}").lower().strip()

            while color_input not in color_map:
                print(f"{ru.UNKNOWN_COLOR}")
                color_input = input(f"{ru.ENTER_COLOR_NAME}").lower().strip()
            return color_map[color_input]

        case "2":
            hex_color = input(f"{ru.ENTER_HEX_CODE}").strip()

            while not (hex_color.startswith('#') and len(hex_color) == 7):
                print(f"{ru.INVALID_HEX_FORMAT}")
                hex_color = input(f"{ru.ENTER_HEX_CODE}").strip()

            while True:
                try:
                    int(hex_color[1:], 16)
                    return hex_color
                except ValueError:
                    print(f"{ru.INVALID_HEX_CHARS}")
                    hex_color = input(f"{ru.ENTER_HEX_CODE}").strip()


def main():
    """
    Main function for drawing fractals with user choice
    """
    print("\n┌──────────────────────────────────────────────┐")
    print(f"│ {ru.FRACTAL_MENU}")
    print("├──────────────────────────────────────────────┤")
    print(f"│ {ru.FRACTAL_1}")
    print(f"│ {ru.FRACTAL_2}")
    print(f"│ {ru.FRACTAL_3}")
    print(f"│ {ru.FRACTAL_4}")
    print(f"│ {ru.FRACTAL_5}")
    print(f"│ {ru.FRACTAL_6}")
    print(f"│ {ru.FRACTAL_7}")
    print(f"│ {ru.FRACTAL_8}")
    print(f"│ {ru.FRACTAL_9}")
    print(f"│ {ru.FRACTAL_10}")
    print("└──────────────────────────────────────────────┘")

    choice = input(f"\n{ru.CHOOSE_FRACTAL}")

    while not (choice.isdigit() and 1 <= int(choice) <= 10):
        print(ru.INVALID_CHOICE)
        choice = input(f"\n{ru.CHOOSE_FRACTAL}")

    choice = int(choice)

    trt.tracer(0)
    trt.speed(0)
    color = get_color_choice()
    trt.color(color)

    match choice:
        case 1:
            print("\n┌─────────────────────────────────────────────────────┐")
            print(f"{ru.FRACTAL_1_REC}")
            print("└──────────────────────────────────────────────────────┘")
            rec_num = input(f"{ru.RECURSION_DEPTH}")
            while not rec_num.isdigit():
                print(ru.INVALID_DEPTH)
                rec_num = input(f"{ru.RECURSION_DEPTH}")
            rec_num = int(rec_num)

            while True:
                try:
                    size = float(input(f"{ru.SIZE}"))
                    break
                except ValueError:
                    print(ru.INVALID_NUM_2)

            trt.penup()
            trt.goto(-200, 0)
            trt.pendown()
            ice_fract_1(rec_num, size)

        case 2:
            print("\n┌─────────────────────────────────────────────────────┐")
            print(f"{ru.FRACTAL_2_REC}")
            print("└──────────────────────────────────────────────────────┘")
            rec_num = input(f"{ru.RECURSION_DEPTH}")
            while not rec_num.isdigit():
                print(ru.INVALID_DEPTH)
                rec_num = input(f"{ru.RECURSION_DEPTH}")
            rec_num = int(rec_num)

            while True:
                try:
                    size = float(input(f"{ru.SIZE}"))
                    break
                except ValueError:
                    print(ru.INVALID_NUM_2)

            trt.penup()
            trt.goto(-400, -100)
            trt.pendown()
            ice_fract_2(rec_num, size)

        case 3:
            print("\n┌─────────────────────────────────────────────────────┐")
            print(f"{ru.FRACTAL_3_REC}")
            print("└──────────────────────────────────────────────────────┘")
            n = input(f"{ru.RECURSION_DEPTH}")
            while not n.isdigit():
                print(ru.INVALID_DEPTH)
                n = input(f"{ru.RECURSION_DEPTH}")
            n = int(n)

            a = input(f"{ru.SIDE_LENGTH}")
            while not a.isdigit():
                print(ru.INVALID_SIDE)
                a = input(f"{ru.SIDE_LENGTH}")
            a = int(a)

            trt.penup()
            trt.goto(-100, 0)
            trt.pendown()

            for _ in range(3):
                koch_triangle(n, a)
                trt.right(120)

        case 4:
            print("\n┌─────────────────────────────────────────────────────┐")
            print(f"{ru.FRACTAL_4_REC}")
            print("└──────────────────────────────────────────────────────┘")
            while True:
                try:
                    size = float(input(f"{ru.INITIAL_SQUARE_SIZE}"))
                    break
                except ValueError:
                    print(ru.INVALID_NUM_2)

            while True:
                try:
                    angle = float(input(f"{ru.ROTATION_ANGLE}"))
                    break
                except ValueError:
                    print(ru.INVALID_NUM_2)

            while True:
                try:
                    k = float(input(f"{ru.K_COEFFICIENT}"))
                    break
                except ValueError:
                    print(ru.INVALID_NUM_2)

            depth = input(f"{ru.RECURSION_DEPTH}")
            while not depth.isdigit():
                print(ru.INVALID_DEPTH)
                depth = input(f"{ru.RECURSION_DEPTH}")
            depth = int(depth)

            trt.penup()
            trt.goto(-100, 0)
            trt.pendown()
            running_square(size, angle, k, depth)

        case 5:
            print("\n┌─────────────────────────────────────────────────────┐")
            print(f"{ru.FRACTAL_5_REC}")
            print("└──────────────────────────────────────────────────────┘")
            rec_num = input(f"{ru.RECURSION_DEPTH}")
            while not rec_num.isdigit():
                print(ru.INVALID_DEPTH)
                rec_num = input(f"{ru.RECURSION_DEPTH}")
            rec_num = int(rec_num)

            while True:
                try:
                    size = float(input(f"{ru.SIZE}"))
                    break
                except ValueError:
                    print(ru.INVALID_NUM_2)

            trt.penup()
            trt.goto(-300, 0)
            trt.pendown()
            mink_curve(rec_num, size)

        case 6:
            print("\n┌─────────────────────────────────────────────────────┐")
            print(f"{ru.FRACTAL_6_REC}")
            print("└──────────────────────────────────────────────────────┘")
            rec_num = input(f"{ru.RECURSION_DEPTH}")
            while not rec_num.isdigit():
                print(ru.INVALID_DEPTH)
                rec_num = input(f"{ru.RECURSION_DEPTH}")
            rec_num = int(rec_num)

            while True:
                try:
                    size = float(input(f"{ru.SIZE}"))
                    break
                except ValueError:
                    print(ru.INVALID_NUM_2)

            trt.penup()
            trt.goto(-100, 0)
            trt.pendown()
            for _ in range(6):
                tangle_6(rec_num, size)
                trt.right(60)

        case 7:
            print("\n┌─────────────────────────────────────────────────────┐")
            print(f"{ru.FRACTAL_7_REC}")
            print("└──────────────────────────────────────────────────────┘")
            while True:
                try:
                    size = float(input(f"{ru.TRIANGLE_SIZE}"))
                    break
                except ValueError:
                    print(ru.INVALID_NUM_2)

            depth = input(f"{ru.RECURSION_DEPTH}")

            while not depth.isdigit():
                print(ru.INVALID_DEPTH)
                depth = input(f"{ru.RECURSION_DEPTH}")
            depth = int(depth)

            trt.penup()
            trt.goto(-200, -150)
            trt.pendown()
            sierpinski(size, depth)

        case 8:
            print("\n┌─────────────────────────────────────────────────────┐")
            print(f"{ru.FRACTAL_8_REC}")
            print("└─────────────────────────────────────────────────────┘")
            iterations = input(f"{ru.RECURSION_DEPTH}")

            while not iterations.isdigit():
                print(ru.INVALID_DEPTH)
                iterations = input(f"{ru.RECURSION_DEPTH}")
            iterations = int(iterations)

            dragon(iterations)

        case 9:
            print("\n┌─────────────────────────────────────────────────────┐")
            print(f"{ru.FRACTAL_9_REC}")
            print("└─────────────────────────────────────────────────────┘")
            iterations = input(f"{ru.RECURSION_DEPTH}")

            while not iterations.isdigit():
                print(ru.INVALID_DEPTH)
                iterations = input(f"{ru.RECURSION_DEPTH}")
            iterations = int(iterations)

            levi(iterations)

        case 10:
            print("\n┌─────────────────────────────────────────────────────┐")
            print(f"{ru.FRACTAL_10_REC}")
            print("└─────────────────────────────────────────────────────┘")

            depth = input(f"{ru.RECURSION_DEPTH}")
            while not depth.isdigit():
                print(ru.INVALID_DEPTH)
                depth = input(f"{ru.RECURSION_DEPTH}")
            depth = int(depth)

            size = input(f"{ru.SIZE}")
            while not size.isdigit():
                print(ru.INVALID_NUM)
                size = input(f"{ru.SIZE}")
            size = int(size)

            trt.penup()
            trt.goto(0, -250)
            trt.setheading(90)
            trt.pendown()

            fractal_tree(size, depth)

        case _:
            print(ru.INVALID_CHOICE)
            return

    print(ru.BEAUTY)
    trt.update()
    trt.done()


if __name__ == '__main__':
    main()
