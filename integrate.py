import math
import random
import miniball
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import copy 

def dist(P_i,c):
    d = {}
    for i in tqdm(range(len(P_i))):
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
    x_i = dist(P_i,c)
    x_m = sorted(x_i.items(), key=lambda item: item[1])
    x_m_list = []
    for key, value in tqdm(x_m):
        x_m_list.append(key)
    i_p[x_m_list[0]] = tuple(c)
    f_p = {}
    for i in tqdm(x_m_list):
        f_p[i] = cart2pol(i_p[i], c)
    return f_p

def attr_fact(x,d):
    return x/d

def gr_points(points):
    groups = {}
    groupnum = 0
    while len(points) > 1:
        groupnum += 1
        key = int(groupnum)
        groups[key] = []
        ref = points.pop(0)
        for i, point in enumerate(points):
            d = get_dist(ref, point)
            if d < con_r:
                groups[key].append(points[i])
                points[i] = None
        groups[key].append(ref)
        points = list(filter(lambda x: x is not None, points))
    return groups

def get_dist(ref, point):
    x1, y1 = ref[0], ref[1]
    x2, y2 = point[0], point[1]
    return math.hypot(x2 - x1, y2 - y1)

def find_attr_clstr(gr,n):
    m = []
    for i in range(len(n)):
        m.append(attr_fact(gr[i], n[i]))
    array = np.array(m)
    max_index = array.argmax()
    return max_index

def connect(a, b):
    l = []
    for v in b:
        for n in a:
            l.append(get_dist(v, n))
    array = np.array(l)
    min_dist = array.argmin()
    d, z, k = l[min_dist], (min_dist)//len(a), (min_dist)%len(a)
    targ_p, first_p = b[z],  a[k]
    
    x, y = first_p[0] - targ_p[0], first_p[1] - targ_p[1]
    rho , phi = con_r, np.arctan2(y, x)
    x, y = rho * np.cos(phi) + targ_p[0], rho * np.sin(phi) + targ_p[1]
    t = (x,y)
    x, y = x - first_p[0],  y - first_p[1]
    for i in a:
        p, q =  x + i[0], y + i[1]
        t = (p, q)
        P_f.append(t)
    return P_f

def sort_dist():
    m = {}
    for i in range(1, len(group)):
        w = []
        for k in group[atr_i]:
            for n in group[i]:
                w.append(get_dist(k, n))
            m[i] = min(w)
    
    sorted_index = []
    sorted_m = sorted(m.items(), key=lambda kv: kv[1])
    for i in sorted_m:
        sorted_index.append(i[0])
    return sorted_index

def start_cluster():
    for i in group[atr_i]:
        P_f.append(i)
    sorted_index.pop(0)


def cluster():
    for i in sorted_index:
        connect(group[i], group[atr_i])
        group[atr_i] = P_f
    
L = 20
no_r = 250  
P_i = [(random.uniform(0, 20), random.uniform(0, 20)) for i in range(no_r)]
P_f = []
mb = miniball.Miniball(P_i)
print('Center', mb.center())
print('Radius', math.sqrt(mb.squared_radius()))
c = mb.center()
r = math.sqrt(mb.squared_radius())
con_r = 1
group = gr_points(copy.deepcopy(P_i)) #dictionary key is index, values are coordinates of points
num_poi = [] #number of points in each cluster
short = [] #shortest distance between center and a point in cluster


if len(P_i) == 1:
    print("The Robots are already connected")
    quit()

for k in (group):
    s = []
    c = []
    if L/con_r < math.sqrt(len(group[k])):
        s.append(k)
    else:
        c.append(k)
    
s_d = {}
for i in s:
    s_d[i] = group[i]
c_d = {}
for i in c:
    c_d[i] = group[i]


print(s,c)






    


