# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты
# для них новыми партами. За каждой партой может
# сидеть два учащихся. Известно количество учащихся
# в каждом из трех классов. Выведите наименьшее число
# парт, которое нужно приобрести для них.

a = int(input("Количество учеников в классе А: "))
b = int(input("Количество учеников в классе B: "))
c = int(input("Количество учеников в классе C: "))

a1 = -a // 2
b1 = -b // 2
c1 = -c // 2
print("На три класса нужно минимум парт:", -(a1 + b1 + c1))
