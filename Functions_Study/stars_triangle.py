# Напишите функцию draw_triangle(fill, base), которая принимает два параметра:
#
# fill – символ заполнитель;
# base – величина основания равнобедренного треугольника;
# а затем выводит его.
#
# Примечание. Гарантируется, что основание треугольника – нечетное число.

# объявление функции
def draw_triangle(fill, base):
    for i in range(1, base+1):
        if i <= base//2+1:
            print(f"{fill*i}")
        else:
            break
    for i in range((base//2), 0, -1):
        print(f"{fill*i}")


# считываем данные
fill = input()
base = int(input())

# вызываем функцию
draw_triangle(fill, base)
