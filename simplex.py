import numpy as np
import scipy as sp

z = [-25, -15]
X = [[2, 2], [3, 1]]
b = [240, 140]

R = (0, None)
T = (0, None)
#M = (0, None)

# ------- Find the Pivot

max_z = z.index(min(z))
RR_list = []
for x in range(len(X)):
    RR = b[x] / X[x][max_z]
    RR_list.append(RR)
min_R = RR_list.index(min(RR_list))


# ------- Iteration

from scipy.optimize import linprog

res = linprog(z, A_ub=X, b_ub=b,  bounds=(R, T), method='simplex', options={"disp": False})  # linear programming p[roblem
#print(res) # print results
print("the pivot is : ",X[min_R][max_z])
print("Iterations   : ",res.nit)
print("Z            : ",res.fun)
