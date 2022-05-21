import smallest
import numpy as np
import matplotlib.pyplot as plt
import flatten

def run():

    # initialize model with interval [0,1]
    x = np.linspace(0, 1)

    # output the expression and calculated rho distribution of flatten model
    print(flatten.flattenModelParamClass.rho)
    y1 = eval(flatten.flattenModelParamClass.rho)

    # output the expression and calculated rho distribution of smallest model
    print(smallest.smallestModelClass.m)
    y2 = eval(smallest.smallestModelClass.m)

    # plot the rho distribution of two models
    plt.plot(x, y1, label='flatten')
    plt.plot(x, y2, label='smallest')
    plt.xlabel('x (m)')
    plt.ylabel('rho (kg/m^3)')
    plt.title('rho vs x')
    plt.legend()
    plt.show()





if __name__ == '__main__':
    run()

