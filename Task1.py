# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии. >

num1 = int(input('Введите число A: '))
num2 = int(input('Введите число B: '))

def stepen(num1, num2):
    if num2 == 0:
        return 1
    if (num2 == 1):
        return num1
    # if (b != 1):
    return num1 * stepen(num1, num2 - 1)

print(f'A в степени B -> {stepen(num1, num2)}')