# Вам доступен текстовый файл prices.txt с информацией о заказе из интернет магазина.
# В нем каждая строка с помощью символа табуляции (\t) разделена на три колонки:
# наименование товара;
# количество товара (целое число);
# цена (в рублях) товара за 11 шт (целое число).
# Напишите программу, выводящую на экран общую стоимость заказа.
file = open('txt_files/prices.txt')
text_in_file = [line.strip().split() for line in file]
total_prices = [int(lines[1])*int(lines[2]) for lines in text_in_file]
print(sum(total_prices))
file.close()

# input in prices.txt
# телефон	4	12500
# бургер	1	500
# курс	1	1400
# подписка	40	9500
# наушники	2	22450
# телефон	2	2500
# ноутбук	5	155000
# диван	100	300