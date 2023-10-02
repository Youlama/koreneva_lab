import sys
from math import sqrt

def get_coef(index, prompt):
    '''
    Читаем коэффициент из командной строки или вводим с клавиатуры

    Args:
        index (int): Номер параметра в командной строке
        prompt (str): Приглашение для ввода коэффицента

    Returns:
        float: Коэффициент квадратного уравнения
    '''
    try:
        # Пробуем прочитать коэффициент из командной строки
        coef_str = sys.argv[index]
    except:
    # Вводим с клавиатуры
        print(prompt)
        coef_str = input()
        # Переводим строку в действительное число
        while True:
            try:
                float(coef_str)
                break
            except:
                print('Ошибка, введите число')
                coef_str = input()
    coef = float(coef_str)
    return coef


def get_roots(a, b, c):
    '''
    Вычисление корней квадратного уравнения

    Args:
        a (float): коэффициент А
        b (float): коэффициент B
        c (float): коэффициент C

    Returns:
        list[float]: Список корней
    '''
    result = []
    D = b * b - 4 * a * c
    print(f"Дискриминант уравнения - {D}")
    if D == 0.0:
        root = -b / (2.0 * a)
        if root > 0:
            result.append(sqrt(root))
            result.append(-sqrt(root))
        elif root == 0:
            result.append(0)
    elif D > 0.0:
        sqD = sqrt(D)
        root1 = (-b + sqD) / (2.0 * a)
        root2 = (-b - sqD) / (2.0 * a)
        if root1 > 0:
            result.append(sqrt(root1))
            result.append(-sqrt(root1))
        elif root1 == 0:
            result.append(0)
        if root2 > 0:
            result.append(sqrt(root2))
            result.append(-sqrt(root2))
        elif root2 == 0:
            result.append(0)
    result = sorted(result)
    return result

def main():
    '''
    Основная функция
    '''
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    # Вычисление корней
    roots = get_roots(a, b, c)
    # Вывод корней
    len_roots = len(roots)
    if len_roots == 0:
        print("Данное уравнение не имеет действительных корней")
    else:
        print("Корни уравнения:")
    for i in range(len_roots):
        print(f"{i + 1} корень = {roots[i]}")

# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()