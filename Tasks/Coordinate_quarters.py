n = int(input())
one, two, three, four = 0, 0, 0, 0
for _ in range(n):
    text = input().split()
    x, y = int(text[0]), int(text[1])

    if '0' in text:
        continue

    if x < 0 and y < 0:
        three += 1
    elif x < 0 and y > 0:
        two += 1
    elif x > 0 and y > 0:
        one += 1
    elif x > 0 and y < 0:
        four += 1

print(f"Первая четверть: {one}\n"
      f"Вторая четверть: {two}\n"
      f"Третья четверть: {three}\n"
      f"Четвертая четверть: {four}\n")
