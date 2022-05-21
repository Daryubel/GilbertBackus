import numpy as np
from sympy import Symbol, integrate, solve


############################################
# class defining the meta parameters
class mainParamClass:
    rho_avg = 5500
    rho_surf = 2800
    phi = 0.33078

############################################
# class defining the symbols used in equation derivation
class flattenModelFunctionClass:

    x = Symbol('x')
    c = Symbol('c')
    f = 1
    h = x

############################################
# main class calculating the flatten model parameters
class flattenModelParamClass:

    # method for cartesian product of (hi, hj)
    def cartesianProduct(i, j):
        f = flattenModelFunctionClass.f
        x = flattenModelFunctionClass.x
        h1 = flattenModelFunctionClass.h**(2*j+3)
        h2 = flattenModelFunctionClass.h**(2*i+3)

        return integrate((h1/f) * (h2/f), (x, 0, 1))

    # method for deciding constant c
    def rhoVal(x, rho):
        c = flattenModelFunctionClass.c
        return eval(str(rho-2800))

    ############################################
    # main parameter calculation body
    d = (mainParamClass.rho_avg / 3, 
        mainParamClass.rho_avg * mainParamClass.phi / 2)

    # H matrix
    matrixH = np.zeros((2,2))
    for j in range(0, 2):
        for i in range(0, 2):
            matrixH[i][j] = cartesianProduct(i, j)
    
    f = ((mainParamClass.rho_surf - mainParamClass.rho_avg), 
       (mainParamClass.rho_surf - (5/2) * mainParamClass.rho_avg * mainParamClass.phi))

    beta = np.dot(np.linalg.inv(matrixH), f)

    # solve for c
    rhoMid = integrate(beta[0]*flattenModelFunctionClass.x**3 + beta[1]*flattenModelFunctionClass.x**5, flattenModelFunctionClass.x) + flattenModelFunctionClass.c
    c = solve(rhoVal(1, rhoMid), flattenModelFunctionClass.c)[0]
    
    ############################################
    # return the symbolized rho expression
    rho = str(integrate(beta[0]*flattenModelFunctionClass.x**3 + beta[1]*flattenModelFunctionClass.x**5, flattenModelFunctionClass.x) + c)

