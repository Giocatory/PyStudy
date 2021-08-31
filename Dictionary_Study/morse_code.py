letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
morse = [
    '.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....',
    '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.',
    '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-',
    '-.--', '--..', '-----', '.----', '..---', '...--', '....-',
    '.....', '-....', '--...', '---..', '----.'
]
info = dict(zip(letters, morse))
n = [i for i in input().upper()]
for i in n:
    if i in letters:
        print(info[i], end=' ')
    else:
        continue
