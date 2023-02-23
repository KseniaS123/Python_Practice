# Петя и Катя – брат и сестра. Петя – студент, а Катя –школьница.
# Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

# x*x - sx + p = 0

s = int(input("Введите сумму чисел: "))
p = int(input("Введите произведение чисел: "))
x_1 = 0
x_2 = 0
d = s * s - 4 * p
if d < 0:
    print("Ошибка")
else:
    x_1 = int(s + d ** 0.5) // 2
    x_2 = s - x_1
    if x_1 * x_2 == p:
        print(x_1, x_2)
    else:
        print("Ошибка: не выполняется условие") 