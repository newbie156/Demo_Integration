n = int(input('Введіть натуральне число: '))
x = int(input('Введіть натуральне число: '))


def numbers(n):
    for number in range(n, x + 1):
        return sum(range(n, x + 1))


summa = sum(range(n, x + 1))
print("Сумма натуральних чисел у заданному проміжку: ", summa)
numbers(n)