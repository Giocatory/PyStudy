matan, inform = int(input()), int(input())
sp1 = []
sp2 = []

for i in range(matan+inform):
    fio = input()
    if fio in sp1:
        sp2.append(fio)
    else:
        sp1.append(fio)

sp = abs(len(sp1) - len(sp2))

if sp == 0:
    print('NO')
else:
    print(sp)
