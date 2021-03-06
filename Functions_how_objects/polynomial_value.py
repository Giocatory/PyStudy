# Многочленом степени nn называется выражение вида
# a_n*x^n + a_(n-1)*x(n-1)+ ... + a_2*x^2+a_1*x+a_0
# где a_n, a_(n-1), ... , a_2, a_1, a_0 — коэффициенты многочлена
# На вход программе на первой строке подаются коэффициенты многочлена,
# разделенные символом пробела и целое число x на второй строке.
# Напишите программу, которая вычисляет значение указанного многочлена
# при заданном значении x.
#
# Формат входных данных
# На вход программе на первой строке подаются коэффициенты многочлена (целые числа),
# разделенные символом пробела и целое число x на второй строке.
#
# Формат выходных данных
# Программа должна вывести одно число — значение указанного многочлена при заданном значении x.
def evaluate_task(coefficients):
    values = list(reversed(coefficients))
    def evaluate_x(x):
        res = 0
        for c in range(len(values)):
            res += values[c]*(x**c)
        return res
    return evaluate_x


values = [int(i) for i in input('nums: ').split()]
extent = int(input('x: '))
function = evaluate_task(values)
print(function(extent))
