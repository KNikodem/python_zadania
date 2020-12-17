import math as m
import random
import numpy as np

def roots():
    a, b, c = [int(x) for x in input("Wprowadz współczynnik a b c: ").split()]
    delta = ((b**2) - (4*a*c))
    x=[]
    if delta > 0:
        x.append((-b + m.sqrt(delta)) / (2*a))
        x.append((-b - m.sqrt(delta)) / (2*a))
    elif delta == 0:
        x.append(-b / (2*a))
    else:
        x.append("Pierwiastek nie istnieje")
    print(x)

def sort():
    sort_numbers = []
    numbers = [random.randint(0, 100) for x in range(100)]
    for i in range(len(numbers)):
        flag = False
        if (i == 0):
            sort_numbers.append(numbers[i])
        else:
            for j in range(len(sort_numbers)):
                if numbers[i] > sort_numbers[j]:
                    sort_numbers.insert(j, numbers[i])
                    flag = True
                    break
            if flag == False:
                sort_numbers.append(numbers[i])
    print(numbers)
    numbers.sort(reverse=True)
    print(numbers)
    print(sort_numbers)
    if numbers == sort_numbers:
        print("Posortowane")
    else:
        print("Błąd")


def scalar():
    a = [1,2,12,4]
    b = [2,4,2,8]
    product = sum([a[x] * b[x] for x in range(len(a))])
    print(product)

def matrix_sum():
    mat1 = [([random.randint(0,100) for i in range(128)]) for j in range(128)]
    mat2 = [([random.randint(0, 100) for i in range(128)]) for j in range(128)]
    res = [([mat1[i][j] + mat2[i][j] for i in range(128)]) for j in range(128)]

def matrix_multiply():
    mat1 = [([random.randint(0, 100) for i in range(8)]) for j in range(8)]
    mat2 = [([random.randint(0, 100) for i in range(8)]) for j in range(8)]
    res =  [([0 for i in range(8)]) for j in range(8)]
    print(mat1)
    print(mat2)
    for i in range(8):
        for j in range(8):
            for k in range(8):
                res[i][j] += mat1[i][k] + mat2[j][k]
    print(res)

def matrix_det():
    mat = [([random.randint(0, 5) for i in range(3)]) for j in range(3)]
    res = [([0 for i in range(8)]) for j in range(8)]
    temp = [([0 for i in range(3)]) for j in range(2)]
    mat_auxilary = mat + temp
    for z  in range(3,5):
        for zz in range(3):
           mat_auxilary[z][zz] = mat[z-3][zz]
    for x in range(i):
        for y in range(i):
            res[x][y] *= res[x+1][y+1] * res[x+2][y+2]
    print(mat_auxilary)
    print(res)



if __name__ == '__main__':
    #roots()
    #sort()
    #scalar()
    #matrix_sum()
    #matrix_multiply()
    matrix_det()
