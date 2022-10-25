# office supplies store
office_supply = [('Бумага офисная', 50, 'грн.', 1, 'уп.'), ('Файлы', 30, 'грн.', 10, 'шт.'),
                 ('Блокнот', 40, 'грн.', 1, 'шт.'), ('Ручка', 10, 'грн.', 1, 'шт.'),
                 ('Карандаш', 10, 'грн.', 1, 'шт.'), ('Текстовый маркер', 40, 'грн.', 4, 'шт.'),
                 ('Степлер', 45, 'грн.', 1, 'шт.'), ('Дырокол', 52, 'грн.', 1, 'шт.')]


def office():
    while True:
        user_input = input('Добавьте товар: '), int(input('Добавьте цену: ')), 'грн.', \
                     int(input('Добавьте кол-во: ')), 'шт.'
        user_input = tuple(user_input)
        stop = input('Наберите off чтобы завершить, нажмите enter чтобы продолжить: ')
        office_supply.append(user_input)
        if stop == 'off':
            break
    return office_supply


print(office())