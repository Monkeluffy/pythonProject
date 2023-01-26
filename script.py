tickets = int(input('Введите количество билетов: '))


ages = []


for i in range(0, tickets):
    input_value = int(input(f'Введите возраст {i + 1} участника: '))
    ages.append(input_value)


    def ticket_prise(ages):
        if ages < 18:
            return 0
        elif 18 <= ages < 25:
            return 990
        elif 25 <= ages:
            return 1390


    total_ = sum(map(ticket_prise, ages))


discount = int(total_ * 0.1)
discounted_prise = int(total_ - discount)
if tickets >= 3:
    print('Полная стоимость билетов: ', total_, "руб.")
    print('Сумма скидки (при регистрации более 3 участников предоставляется скидка 10%): ', discount, "руб.")
    print('Общая стоимость билетов со скидкой: ', discounted_prise, "руб.")
else:
    print('Общая стоимость билетов: ', total_, "руб.")