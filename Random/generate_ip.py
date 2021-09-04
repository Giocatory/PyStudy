from random import choice as cho


def generate_ip():
    interval = list(range(0, 256))
    return f"{cho(interval)}.{cho(interval)}.{cho(interval)}.{cho(interval)}"


print(generate_ip())
