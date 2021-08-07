s = input()
ss = input()

for i in range(len(s)):
    if i == len(s)-1:
        print(s[i])
        break
    print(s[i]+ss, end='')

