# Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.

# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18

# 6 12

# n = {2, 4, 6, 8, 10, 12, 10, 8, 6, 4, 2}
# m = {3, 6, 9, 12, 15, 18}

n = int(input("Введите количество элементов первого множества: "))
m = int(input("Введите количество элементов второго множества: "))
spisok_1 = []
spisok_2 = []
for i in range(n):
    num_1 = int(input())
    spisok_1.append(num_1)
print(*spisok_1)
for j in range(m):
    num_2 = int(input())
    spisok_2.append(num_2)
print(*spisok_2)
print(*sorted(set(spisok_1).intersection(set(spisok_2))))