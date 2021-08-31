# Напишите программу, которая будет превращать натуральное число в строку,
# заменяя все цифры в числе на слова:
# 0 на zero;
# 1 на one;
# 2 на two;
# 3 на three;
# 4 на four;
# 5 на five;
# 6 на six;
# 7 на seven;
# 8 на eight;
# 9 на nine.
my_dict = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"
}
n = [int(i) for i in input()]
for i in n:
    print(my_dict[i], end=' ')
