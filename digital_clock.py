how_many_minutes_passed = int(input('Сколько минут прошло (от 00:00)?: '))
hour = 0
days = 0
while how_many_minutes_passed >= 60:
    hour += 1
    how_many_minutes_passed -= 60
    if hour >= 24:
        hour = 0
        days += 1
print(f"Прошло {days} дней и сейчас время: {hour}:{how_many_minutes_passed}")
