import math


def quadratic_equation(a, b, c):
    x1 = None
    x2 = None
    if a == 0:
        return 'a can\'t be equal to 0 by default'

    def calc_rezult(a, b, c):

        nonlocal x1, x2
    discr = (b ** 2) - (4 * a * c)
    print('Discriminant = ', discr)

    if discr < 0:
        return 'no roots'
    if discr == 0:
        x1 = b * b / (2 * a)
        x2 = -b * b / (2 * a)
        return x1, x2
    else:
        x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        return x1, x2


print(quadratic_equation(float(input('a = ')), float(input('b = ')), float(input('c = '))))

# програма наче рахує правильно, незважаючи на ці помилки. Можна їх якось усунути?
# Local variable 'x1' value is not used
# Local variable 'x2' value is not used
# Local function 'calc_rezult' is not used
# Parameter 'a' value is not used
# Shadows name 'a' from outer scope
# Parameter 'b' value is not used
# Shadows name 'b' from outer scope
# Parameter 'c' value is not used
# Shadows name 'c' from outer scope
