# Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.

num = int(input("Введите номер билета: "))
sum_1 = 0
sum_2 = 0
while num != 0:
    n = num % 10
    if num > 999:
        sum_2 = sum_2 + n
    else:
        sum_1 = sum_1 + n
    num = num // 10
if sum_1 == sum_2:
    print("Счастливый")
else:
    print("Несчастливый")