# В школе решили набрать три новых математических класса.
# Так как занятия по математике у них проходят в одно и то же время,
# было решено выделить кабинет для каждого класса и купить в них новые парты.
# За каждой партой может сидеть не больше двух учеников.
# Известно количество учащихся в каждом из трёх классов.
# Сколько всего нужно закупить парт чтобы их хватило на всех учеников?
# Программа получает на вход три натуральных числа:
# количество учащихся в каждом из трех классов.

number_of_first_grade_students = int(input('Количество школьников первого класса: '))
number_of_second_grade_students = int(input('Количество школьников второго класса: '))
number_of_third_grade_students = int(input('Количество школьников третьего класса: '))

how_many_desks_are_needed_equally = (number_of_first_grade_students // 2
                                     + number_of_second_grade_students // 2
                                     + number_of_third_grade_students // 2
                                     + number_of_first_grade_students % 2
                                     + number_of_second_grade_students % 2
                                     + number_of_third_grade_students % 2)
print(how_many_desks_are_needed_equally)
