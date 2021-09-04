import random

length = 15
all_letters = list(range(97, 123)) + list(range(65, 91))
password = [chr(random.choice(all_letters)) for _ in range(length)]
print(*password, sep='')