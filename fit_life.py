WATER_PER_KG = 30
ML_PER_LITER = 1000

# ввод данных пользователя и проверка на корректность
while True:
    user_name = input('Привет! Я твой персональный помощник! Как тебя зовут?')
    if user_name != '':
        break
    else:
        print('Введите имя')

while True:
    user_age = input('Укажите ваш возраст цифрой, например "18"')
    if user_age.isdigit():
        user_age = int(user_age)
        break
    else:
        print('Вы ввели не цифру')

while True:
    try:
        user_weight = float(input('Укажи свой вес в килограммах:'))
        break
    except ValueError:
        print('Нужно указать вес в килограммах!')

while True:
    user_height = input('Теперь добавь свой рост в метрах(например, 1.75):')
    if '.' in user_height:
        user_height = float(user_height)
        break
    else:
        print('Используй точку (например, 1.75)')

# расчёт ИМТ с округлением до одного знака после запятой
bmi = round(user_weight / (user_height ** 2), 1)

# расчёт нормы воды в милилитрах
water_ml = user_weight * WATER_PER_KG

# перевод нормы воды в литры
water_l = water_ml / ML_PER_LITER

# вывод рекомендаций
print(
    f'Персональные рекомендации для {user_name} (возраст {user_age}) готовы!\n'
    f'{'-' * 70}\n'
    f'Твой ИМТ(индекс массы тела): {bmi}\n'
    f'Рекомендуемая норма воды: {water_l:.1f} л. в день\n'
    f'{'-' * 70}\nРасчёт окончен! Будьте здоровы!'
)
