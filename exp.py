import random

seven_numbers = set()

while True:
    seven_numbers.add(random.choice(list(range(1, 50))))
    if len(seven_numbers) == 7:
        break

print(*list(sorted(seven_numbers)))