# TODO: Maximum recursion depth exceeded with D > 100.000.000

import sys
from math import sqrt

def obtenerFraccionContinua(A, x):
    a0 = int(sqrt(x))
    d = 1
    m = 0
    a = 0

    prim = True

    if a0*a0 != x:
        while (a != 2*a0):
            m = d*a - m;
            d = (x - m * m) / d;
            a = int((a0 + m) / d);
            if not prim:
                A.append(a)
            prim = False


def result(A, num, den, i, maximo):
    if (i >= maximo):
        return num*A[i] + 1, A[i]
    else:
        rnum, rden = result(A, den, A[i+1], i+1, maximo)
        num = num*rnum + rden
        den = rnum
        return num, den


def main():
    print "Pell Equation"
    print "x^2 - D*y^2 = 1"
    print " "
    if len(sys.argv) > 1:
        d = int(sys.argv[1])
    else:
        d = int(raw_input("Enter the desired D to solve for: "))

    A = []
    a0 = int(sqrt(d))
    #A.append(a0)
    obtenerFraccionContinua(A, d)

    longCiclo = len(A)-1
    p=1
    q=0

    if longCiclo > 0:
        if longCiclo%2 == 0:
            p, q = result(A, A[0], A[1], 1, longCiclo-2)
        else:
            A += A[1:] +A[1:]
            p, q = result(A, A[0], A[1], 1, 2*longCiclo-1)

    print "--------------------------------------------"
    print "Fundamental solution for D = " + str(d) + ": "
    print "x = " + str(p)
    print "y = " + str(q)


if __name__ == '__main__':
    main()
