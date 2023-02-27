def count_system(x1, x2, x3):
    equation_1 = 2.01*x1 - 0.53*x2 + 1.13*x3
    equation_2 = -0.53 * x1 + 1.62 * x2 - 1.03 * x3
    equation_3 = 1.13 * x1 - 1.03 * x2 + 2.34 * x3
    return equation_1, equation_2, equation_3


def new_x1(x2, x3):
    return (-2.09 + 0.53*x2 - 1.13*x3)/2.01


def new_x2(x1, x3):
    return (0.39 + 0.53*x1 + 1.03*x3)/1.62


def new_x3(x1, x2):
    return (2.13 - 1.13*x1 + 1.03*x2)/2.34


def compute(eps=1e-5):
    prev_x1 = 0
    prev_x2 = 0
    prev_x3 = 0

    curr_x1 = -2.09/2.01
    curr_x2 = 0.39/1.62
    curr_x3 = 2.13/2.34

    while (abs(curr_x1 - prev_x1) > eps) and (abs(curr_x2 - prev_x2) > eps) and (abs(curr_x3 - prev_x3) > eps):
        prev_x1 = curr_x1
        prev_x2 = curr_x2
        prev_x3 = curr_x3

        curr_x1 = new_x1(curr_x2, curr_x3)
        curr_x2 = new_x2(curr_x1, curr_x3)
        curr_x3 = new_x3(curr_x1, curr_x2)

    return curr_x1, curr_x2, curr_x3


def check(x1, x2, x3):
    right_answers = [-2.09, 0.39, 2.13]
    equations = count_system(x1, x2, x3)
    for equation, answer in zip(equations, right_answers):
        print(f"The result of computing: {round(equation, 5)}, the right answer: {answer}")


def test():
    x1, x2, x3 = compute()
    check(x1, x2, x3)


test()
