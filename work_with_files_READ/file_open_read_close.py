file = open('txt_files/example.txt')
for line in file:
    print(line.strip())
file.close()

print()

with(open('txt_files/example.txt', 'r+')) as file:
    for line in file:
        print(line.strip())
