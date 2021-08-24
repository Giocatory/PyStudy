def next_row(lines):
    lines = [1] + lines
    for i in range(1, len(lines) - 1):
        lines[i] += lines[i + 1]
    return lines


row = []
n = int(input()) + 1
for i in range(n):
    row = next_row(row)
    if len(row) == n:
        print(row)


# def next_row(lines):
#     lines = [1] + lines
#     for i in range(1, len(lines) - 1):
#         lines[i] += lines[i + 1]
#     return lines
#
#
# row = []
# n = int(input())
# for i in range(n):
#     row = next_row(row)
#     print(*row)
