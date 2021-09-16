with open('input.txt', 'r') as input, open('output.txt', 'w') as output:
    lines_in_file = len(input.readlines())
    input.seek(0)
    for i in range(lines_in_file):
        print(f"{i+1}) {input.readline().strip()}", file=output)
