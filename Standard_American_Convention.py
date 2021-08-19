# 10000000000
# 10,000,000,000

text = input()
new_text = ''
count = 0
for i in range(1, len(text)+1):
    if count == 3:
        new_text += ','+text[-i]
        count = 1
    else:
        new_text += text[-i]
        count += 1
print(new_text[::-1])
