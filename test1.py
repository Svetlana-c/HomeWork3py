def sum_odd_pos(a):
    sum = 0
    for i in range(len(a)):
        if i % 2 != 0:
            sum += a[i]
    print(f'Сумма равна: {sum}')
a = [2,3,5,9,3]
sum_odd_pos(a)
a = list(map(int, input("Введите числа через пробел:\n").split()))
sum_odd_pos(a)