import random


def generate_password(length):
    all_letters = list("abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ") + list("23456789")
    password = [random.choice(all_letters) for _ in range(length)]
    print(*password, sep='')


def generate_passwords(count, length):
    for _ in range(count):
        generate_password(length)


n, m = int(input()), int(input())
generate_passwords(n, m)
