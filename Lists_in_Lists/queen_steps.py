from math import fabs

board = [['.'] * 8 for _ in range(8)]

dct = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}

text = input()
v = text[0]
g = int(text[1])

board[dct[v]][g - 1] = 'Q'

for i in range(ord('a'), ord('h') + 1):
    for j in range(1, 9):
        if (i != ord(v) or j != g) and ((i == ord(v) or j == g) or (abs(i - ord(v)) == abs(j - g))):
            board[dct[chr(i)]][j - 1] = '*'

board = list(zip(*board))
for x in reversed(board):
    print(' '.join(x))