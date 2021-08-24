n = int(input())
lines = [input() for i in range(n)]
error_line = [i for i in range(len(lines)) if ['a', 'n', 't', 'o', 'n'] in lines[i]]
print(*error_line)
