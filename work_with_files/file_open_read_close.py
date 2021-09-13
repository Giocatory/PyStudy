file = open('example.txt')
for line in file:
    print(line.strip())
file.close()

print()

with(open('example.txt', 'r+')) as file:
    for line in file:
        print(line.strip())
