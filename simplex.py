import numpy as np
import scipy as sp


print("                 Welcome to Simplex Algorithm                 ")
print("\n \n")
print("                    Enter Values of MaxZ                      ")
nbr_var = int(input("                     How many variable? \n"))

z = []
for i in range(nbr_var):
    print("X",i+1," : ", end ="")
    z_var = int(input())    
    z.append(-z_var)

nbr_eq = int(input("                     How many equation? \n "))

X = []
b = []
for j in range(nbr_eq):
    print("Coef of equation",j+1," : ")
    xi = []
    x11 = int(input())
    x22 = int(input())
    b_input = int(input("B = "))
    xi.append(x11)
    xi.append(x22)
    X.append(xi)
    b.append(b_input)

#z = [-400, -500] # Max Z
#X = [[4, 6], [8, 3]] 
#b = [60, 240] # <b
print(z)
print(X)
print(b)

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
