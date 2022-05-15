import math
import time


def fib_1(n):
    if n == 0:
        return 0
    if n== 1:
        return 1
    return fib_1(n - 1) + fib_1(n - 2)

def cal_power(n):
    if n == 0:
        return 1
    if n % 2 == 1:
        return cal_power((n - 1) / 2) ** 2 * ((math.sqrt(5) + 1) / 2)
    if n % 2 == 0:
        return cal_power(n / 2) ** 2

def fib_2(n):
    return int(cal_power(n) / math.sqrt(5) + 0.5)

def fib_3(n):
    ls = []
    if n == 0:
        return 0
    if n == 1:
        return 1
    for i in range(n + 1):
        if i == 0:
            ls.append(0)
            continue
        if i == 1:
            ls.append(1)
            continue
        ls.append(ls[i - 2] + ls[i - 1])
    return ls[n]


def cal_matrix_mul(m, n):
    start = [[0, 0],[0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                start[i][j] += m[i][k] * n[k][j]
    return start

matr = [[1, 1], [1, 0]]
def cal_matrix_power(n):
    if n == 1:
        return matr
    if n % 2 == 0:
        tmp = cal_matrix_power(n / 2)
        return cal_matrix_mul(tmp, tmp)
    if n % 2 == 1:
        tmp = cal_matrix_power((n - 1) / 2)
        return cal_matrix_mul(cal_matrix_mul(tmp, tmp), matr)

def fib_4(n):
    return cal_matrix_power(n + 1)[1][1]

def main():
    print("{:=^100}".format("this is first algorithm"))
    for i in range(40):
        starttime = time.time()
        num = fib_1(i)
        endtime = time.time()
        t = (endtime - starttime)

        
        print("n = {:^5}, time = {:^16.5f} us = {:16.5f} ms = {:16.5f} s".format(i, t * 1000000, t * 1000, t))
    print("")

    print("{:=^100}".format("this is second algorithm"))
    for i in range(0, 1000, 25):
        starttime = time.time()
        num = fib_2(i)
        endtime = time.time()
        t = (endtime - starttime)
        
        print("n = {:^5}, time = {:^16.5f} us = {:16.5f} ms = {:16.5f} s".format(i, t * 1000000, t * 1000, t))
    print("")

    print("{:=^100}".format("this is third algorithm"))
    for i in range(0, 1000, 25):
        starttime = time.time()
        num = fib_3(i)
        endtime = time.time()
        t = (endtime - starttime)
        
        print("n = {:^5}, time = {:^16.5f} us = {:16.5f} ms = {:16.5f} s".format(i, t * 1000000, t * 1000, t))
    print("")

    print("{:=^100}".format("this is fourth algorithm"))
    for i in range(0, 1000, 25):
        starttime = time.time()
        num = fib_4(i)
        endtime = time.time()
        t = (endtime - starttime)
        
        print("n = {:^5}, time = {:^16.5f} us = {:16.5f} ms = {:16.5f} s".format(i, t * 1000000, t * 1000, t))
    print("")

if __name__ == "__main__":
    main()