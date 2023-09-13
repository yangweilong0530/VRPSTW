from gurobipy import Model,GRB,quicksum
from matplotlib import pyplot as plt
import numpy as np

xc=[0,5,1,6,2,4,7]
yc=[0,8,9,3,6,2,1]
q=[0,1,1,1,1,1,1]
e=[0,100,50,70,63,22,100]
l=[1000,300,160,200,360,400,500]
Cij=[[np.hypot(xc[i]-xc[j],yc[i]-yc[j]) for j in range(len(xc))] for i in range(len(xc))]
tij=[[j*10 for j in i]for i in Cij]
C1=1
C2=1
C3=10
Q=10
model=Model()
plt.scatter(xc,yc,s=10)
plt.show()