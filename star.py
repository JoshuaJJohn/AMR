import math
import random
import miniball
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm


no_r = 10_00
P_i = [(random.uniform(0, 20), random.uniform(0, 20)) for i in tqdm(range(no_r))]
mb = miniball.Miniball(P_i)
print('Center', mb.center())
print('Radius', math.sqrt(mb.squared_radius()))
c = mb.center()
r = math.sqrt(mb.squared_radius())
con_r = 1
#c = np.repeat(mb.center(), [1, 3], axis=0)
def dist(P_i,c):
    d = {}
    for i in range(len(P_i)):
        e = math.dist(P_i[i],c)
        d[i] = e
    return d


def plotsc(P_i):
    x, y = zip(*P_i)
    plt.scatter(x, y)

def cart2pol(f, c):
    x, y = f
    x = x - c[0]
    y = y - c[1]
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)

    if rho > con_r:
        rho = con_r
    
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    x = x + c[0]
    y = y + c[1]
    return(x, y)

def starcon():
    i_p = {}
    for i in tqdm(range(len(P_i))):
        i_p[i] = P_i[i]
    
    #print("initial position", i_p)

    x_i = dist(P_i,c)

    x_m = sorted(x_i.items(), key=lambda item: item[1])
    x_m_list = []
    for key, value in tqdm(x_m):
        x_m_list.append(key)
    #print("key of sorted distances", x_m_list)

    i_p[x_m_list[0]] = tuple(c)
    #print("after moving closest robot to the center of SEC", i_p)

    f_p = {}

    for i in tqdm(x_m_list):
        f_p[i] = cart2pol(i_p[i], c)
    #print(f_p)

    plotsc(list(i_p.values()))
    plotsc(list(f_p.values()))
    plt.axis('scaled')
    plt.show()
    


    
    #print(x_i)


starcon()




    


