data = [
    (19542209, 'New York'),
    (4887871, 'Alabama'),
    (1420491, 'Hawaii'),
    (626299, 'Vermont'),
    (1805832, 'West Virginia'),
    (39865590, 'California'),
    (11799448, 'Ohio'),
    (10711908, 'Georgia'),
    (10077331, 'Michigan'),
    (10439388, 'Virginia'),
    (7705281, 'Washington'),
    (7151502, 'Arizona'),
    (7029917, 'Massachusetts'),
    (6910840, 'Tennessee')
]
data.sort(key=lambda x: x[1][-1], reverse=True)
for i in data:
    print(f"{i[1]}: {i[0]}")
