def lcm(a, b, p):
    # наименьшее общее кратное двух натуральных чисел
    if a == 0:
        return p // b
    return lcm(b % a, a, p)


try:
    number_a = int(input('Число а: '))
    number_b = int(input('Число b: '))
except ValueError:
    exit('Ввести можно только натуральные числа')

if number_a < 1 or number_b < 1:
    exit('Ввести можно только натуральные числа')

print('Наименьшее общее кратное чисел а и b:', lcm(number_a, number_b, number_a * number_b))
