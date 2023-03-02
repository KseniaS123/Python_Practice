# Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def degree(a, b):
    if b == 0:
        return 1
    if b < 0:
        return round(degree(a, b + 1) * 1 / a, 4)
    return degree(a, b - 1) * a

print(degree(int(input()), int(input())))