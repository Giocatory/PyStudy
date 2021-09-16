# Вам доступен CSV-файл data.csv, содержащий информацию в csv формате.
# Напишите функцию read_csv для чтения данных из этого файла.
# Она должна возвращать список словарей, интерпретируя первую строку как имена ключей,
# а каждую последующую строку как значения этих ключей.
# Примечание 1. Вызывать функцию read_csv не нужно.
# Примечание 2. Функции read_csv не должна принимать аргументов.
# Примечание 3. Считайте, что все ключи и значения по этим ключам в результирующем словаре
# имеют строковый тип (str).
def read_csv():
    with open('txt_files/data.csv') as file:
        lines_in_file = len(file.readlines())
        file.seek(0)
        keys = (file.readline().strip()).split(',')
        list_of_dicts = [dict(zip(keys, (file.readline().strip()).split(','))) for _ in range(lines_in_file - 1)]
        return list_of_dicts

print(*read_csv(), sep='\n')
