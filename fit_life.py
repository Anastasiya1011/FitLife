import sys
import io


sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


WATER_PER_KG = 30
ML_PER_LITER = 1000

# ввод данных пользователя и проверка на корректность
user_name = input('Привет! Я твой персональный помощник! Как тебя зовут?')

try:
    user_age = int(input('Сколько тебе лет?'))
except ValueError:
    user_age = int(input('Укажите ваш возраст цифрой, например "18"'))

try:
    user_weight = float(input('Укажи свой вес в килограммах:'))
except ValueError:
    user_weight = float(input('Нужно указать вес в килограммах:'))

try:
    user_height = input('Теперь добавь свой рост в метрах(например, 1.75):')
    if '.' not in user_height:
        raise ValueError
except ValueError:
    user_height = float(input(
        'Используй точку, чтобы указать рост в метрах (например, 1.70):'))
else:
    user_height = float(user_height)

# расчёт ИМТ с округлением до одного знака после запятой
bmi = round(user_weight / (user_height ** 2), 1)

# расчёт нормы воды в милилитрах
water_ml = user_weight * WATER_PER_KG

# перевод нормы воды в литры
water_l = round(water_ml / ML_PER_LITER, 1)

# вывод рекомендаций
print(f"""
Итак, персональные рекомендации готовы!
{'-' * 50}
Имя пользователя: {user_name}, возраст: {user_age}
Твой ИМТ(индекс массы тела): {bmi}
Рекомендованная норма воды в день: {water_l} л.
{'-' * 50}
Расчёт окончен! Будьте здоровы!
""")
