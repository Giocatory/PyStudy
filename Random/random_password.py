import random
import string

length = 15
all_letters = list(string.ascii_letters) + list(string.digits) + list(string.punctuation)
password = [random.choice(all_letters) for _ in range(length)]
print(*password, sep='')