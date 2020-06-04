'''
Реалізувати програму, в якій кожен з алгоритмів сортування оформити як окрему
функцію. Проілюструвати механізм використання параметрів різних типів. Забезпечити
підрахунок числа необхідних порівнянь, числа обмінів і часу роботи кожної функції,
сформувавши функції оцінки ефективності методів сортування.
Постолович А.С. 122-В
'''
import numpy as np
import random
import timeit

i = input("How input?\n"
        "Random - 1, from keyboard - not 1: ") #обираємо метод створення масиву
if i == '1':
    A = np.zeros(100000, dtype=int)
    for j in range(100000):
        A[j] = random.randint(-200000, 200000)
else:
    A = np.zeros(30, dtype=int)
    for j in range(30):
        A[i] = int(input("Input number:"))
print(A)

#створюємо окрему функцію для кожного з методів по зростанню і спаданню
def buble_sort_up():
    global change_b_up
    global comparison_b_up
    change_b_up = 0
    comparison_b_up = 0
    for i in range(len(A)):  #сортування бульбашкою за зростанням
        for j in range(len(A) - 1, i - 1, -1):
            comparison_b_up += 1
            if (A[j - 1] > A[j]):
                change_b_up += 1
                A[j], A[j - 1] = A[j - 1], A[j]
    print(f'Number of exchanges - {change_b_up}')
    print(f'Number of comparisons - {comparison_b_up}')
    print(A)

def buble_sort_down():
    global change_b_down
    global comparison_b_down
    change_b_down = 0
    comparison_b_down = 0
    for i in range(len(A)):  #сортування бульбашкою за спаданням
        for j in range(len(A) - 1, i - 1, -1):
            comparison_b_down += 1
            if (A[j - 1] < A[j]):
                change_b_down += 1
                A[j], A[j - 1] = A[j - 1], A[j]
    print(f'Number of exchanges - {change_b_down}')
    print(f'Number of comparisons - {comparison_b_down}')
    print(A)

def select_sort_up():
    global change_s_up
    global comparison_s_up
    change_s_up = 0
    comparison_s_up = 0
    for i in range(len(A) - 1):  #сортування методом вибору за зростанням
        min = i
        for j in range(i + 1, len(A)):
            comparison_s_up += 1
            if A[j] < A[min]:
                change_s_up += 1
                min = j
        A[i], A[min] = A[min], A[i]
    print(f'Number of exchanges - {change_s_up}')
    print(f'Number of comparisons - {comparison_s_up}')
    print(A)

def select_sort_down():
    global change_s_down
    global comparison_s_down
    change_s_down = 0
    comparison_s_down = 0
    for i in range(len(A) - 1):  #сортування методом вибору за спаданням
        min = i
        for j in range(i + 1, len(A)):
            comparison_s_down += 1
            if A[j] > A[min]:
                change_s_down += 1
                min = j
        A[i], A[min] = A[min], A[i]
    print(f'Number of exchanges - {change_s_down}')
    print(f'Number of comparisons - {comparison_s_down}')
    print(A)

def insertion_sort_up():
    global change_i_up
    global comparison_i_up
    change_i_up = 0
    comparison_i_up = 0
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and key < A[j]: #сортування методом вставки за зростанням
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key
    print(f'Number of exchanges - {change_i_up}')
    print(f'Number of comparisons - {comparison_i_up}')
    print(A)

def insertion_sort_down():
    global change_i_down
    global comparison_i_down
    change_i_down = 0
    comparison_i_down = 0
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and key > A[j]: #сортування методом вставки за спаданням
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key
    print(f'Number of exchanges - {change_i_down}')
    print(f'Number of comparisons - {comparison_i_down}')
    print(A)

#обираємо метод для сортування по зростанню
m_1 = input("Select the method to sort up?\n"
        "Buble - 1, select - 2, insertion - other digit: ")
if m_1 == '1':
    buble_sort_up()
elif m_1 == '2':
    select_sort_up()
else:
    insertion_sort_up()

#обираємо метод для сортування по спаданню
m_2 = input("Select the method to sort down?\n"
        "Buble - 1, select - 2, insertion - other digit: ")
if m_2 == '1':
    buble_sort_down()
elif m_2 == '2':
    select_sort_down()
else:
    insertion_sort_down()

#виводимо час виконання програми
t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(f'The program lasted {t} seconds')