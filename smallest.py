from sympy import Symbol, integrate
import numpy as np


class mainParamClass:
    rho_avg = 5500
    phi = 0.33078


class smallestModelFunctionClass:

    x = Symbol('x')
    f = 1
    g = x**2

class smallestModelParamClass:

    def cartesianProduct(i, j):
        f = smallestModelFunctionClass.f
        g1 = smallestModelFunctionClass.g**(j+1)
        g2 = smallestModelFunctionClass.g**(i+1)
        x = smallestModelFunctionClass.x

        return integrate((g1/f) * (g2/f), (x, 0, 1))

    d = (mainParamClass.rho_avg / 3, 
        mainParamClass.rho_avg * mainParamClass.phi / 2)

    matrixG = np.zeros((2,2))
    for j in range(0, 2):
        for i in range(0, 2):
            matrixG[i][j] = cartesianProduct(i, j)

    a = np.dot(np.linalg.inv(matrixG), d)


class smallestModelClass:

    def run():
        print(smallestModelParamClass.matrixG)
        print(smallestModelParamClass.a)

    g_over_f = (smallestModelFunctionClass.g**1/smallestModelFunctionClass.f**2, smallestModelFunctionClass.g**2/smallestModelFunctionClass.f**2)
    x = smallestModelFunctionClass.x

    m = str(np.dot(smallestModelParamClass.a, g_over_f))




