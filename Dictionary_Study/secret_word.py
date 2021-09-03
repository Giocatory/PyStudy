text = input()  # *!*!*?
s = {i: str(text.count(i)) for i in text}  # {'*': '3', '!': '2', '?': '1'}
n = int(input())  # 3
sc = dict([input().split(': ') for _ in range(n)])  # {'а': '3', 'н': '2', 'с': '1'}

for i in text:
    for k,v in sc.items():
        if s.get(i) == v:
            print(k, end='')
# ананас
