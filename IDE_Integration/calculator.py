import math


def run():
    return float(input('Введите число: ')), float(input('Введите число: '))


def root():
    return float(input('Введите число: '))


def f_root():
    return int(input('Введите число: '))


def calculate():
    while True:
        operation = input('''Введите знак операции:
+
- 
* 
/
%
^ 
√
∛ 
sin
cos
tan
degrees
radians
π
e
log
factorial
off - завершить программу: ''')
        if operation == '+':
            print(add())
        elif operation == '-':
            print(substract())
        elif operation == '*':
            print(multiply())
        elif operation == '/':
            print(divide())
        elif operation == '%':
            print(mod())
        elif operation == '^':
            print(exponentiate())
        elif operation == '√':
            print(sqrt())
        elif operation == '∛':
            print(cbrt())
        elif operation == 'sin':
            print(sin())
        elif operation == 'cos':
            print(cos())
        elif operation == 'tan':
            print(tan())
        elif operation == 'degrees':
            print(degrees())
        elif operation == 'radians':
            print(radians())
        elif operation == 'π':
            print(pi())
        elif operation == 'e':
            print(e_num())
        elif operation == 'log':
            print(log())
        elif operation == 'factorial':
            print(factorial())
        elif operation == 'log10':
            print(log_10())

        else:
            if operation == 'off':
                exit()


def add():
    a, b = run()
    return a + b


def substract():
    a, b = run()
    return a - b


def multiply():
    a, b = run()
    return a * b


def divide():
    a, b = run()
    if b != 0:
        return a / b
    else:
        return 'Деление на 0!'


def mod():
    a, b = run()
    return a % b


def exponentiate():
    a, b = run()
    return pow(a, b)


def sqrt():
    a = root()
    return math.sqrt(a)


def cbrt():
    a = root()
    return math.pow(a, 1/3)


def sin():
    a = root()
    return math.sin(a)


def cos():
    a = root()
    return math.cos(a)


def tan():
    a = root()
    return math.tan(a)


def degrees():
    a = root()
    return math.degrees(a)


def radians():
    a = root()
    return math.radians(a)


def pi():
    return math.pi


def e_num():
    return math.e


def log():
    a, b = run()
    return math.log(a, b)


def factorial():
    a = f_root()
    return math.factorial(a)


def log_10():
    a = root()
    return math.log10(a)


calculate()
