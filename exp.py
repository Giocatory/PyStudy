import random
import string

upper = set("ABCDEFGHJKLMNPQRSTUVWXYZ")
digits = set(string.digits)


def valid(s):
    s = set(s)
    invalid = s.difference(upper, digits)
    both = s.intersection(upper) and s.intersection(digits)
    return bool(both and not invalid)


def generate_password(length):
    pss = ''
    while True:
        all_letters = list("abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ") + list("23456789")
        password = [random.choice(all_letters) for _ in range(length)]
        for i in password:
            pss += i
        if not(pss.isupper() or pss.islower()or pss.isdigit()or pss.isalpha() or len(pss) == length):
            break
    print(pss)
    pss = ''


def generate_passwords(count, length):
    for _ in range(count):
        generate_password(length)


n, m = int(input()), int(input())
generate_passwords(n, m)
