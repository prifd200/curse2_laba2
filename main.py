import numpy as np


def factorial(n,oldfact):
    if oldfact !=1:
        fact = oldfact * (2*n) * (2*n - 1)
    else:
        return 1
    return fact

def algorithm(n, X,oldfact):
    fact = 2 * n + 1
    currentfact = factorial(fact, oldfact)                                   # Вычисление факториала
    det = np.linalg.det(np.linalg.matrix_power(X, (2 * n + 1)))              # Вычисляем определитель
    res = det/factorial(n, fact) * (-1)**n
    return res, currentfact

try:
    while True:
        k = int(input("Введите ранг матрицы от 3 до 50  k = "))
        if k >= 3 and k <= 50:
            break
        else:
            print("Ваше число не входит в данный диапазон")
    while True:
        t = int(input("Введите количество знаков после запятой от 1 до 20 t ="))
        if t>=1 and t <= 20:
            break
        else:
            print("Ваше число не входит в данный диапазон")
    print(f"Ранг матрицы k = {k}, Точность вычислений t знаков = {t}\n")
    X = np.random.randint(-10, 10, (k,k))                                         # Задаём матрицу
    X = X / 10
    print(X)
    n = 1
    summ = 0
    oldfact = 1
    predsumma = 0
    while True:
        predsumma, oldfact = algorithm(n, X, oldfact)
        summ += predsumma
        n += 1
        if abs(predsumma) < (10 ** (-t)):
            print("сумма= ", summ)
            break
except:
    print("Произошла ошибка")

