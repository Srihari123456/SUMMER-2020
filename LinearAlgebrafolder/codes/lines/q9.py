import numpy as np
import matplotlib.pyplot as plt
import math 
A = np.array([3,-1])
B = np.array([4,-2])
C = np.array([0,2])
D = np.array([5,-3])
#Generate line points
def line_gen(A,B):
  len =10
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB
#y +2  = -1(x -4)
#y+2=4-x
#x+y=2

def xang(A,B):
    theta = (B[1]-A[1])/(B[0]-A[0])
    arctan = np.arctan(theta)
    arctan *= (180/3.14)
    if arctan < 0:
        arctan = 180 + arctan
    return math.ceil(arctan)
E = np.array([0,0])
F = np.array([5,0])
x_AB = line_gen(C,D)
xaxis = line_gen(E,F)


plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 + 0.1), B[1] * (1 - 0.1) , 'B')

plt.plot(x_AB[0,:],x_AB[1,:],label="line")
plt.plot(xaxis[0,:],xaxis[1,:],label="x-axis")
print("Angle between line and x-axis",xang(A,B),"degree")
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
#plt.axis('equal')

#if using termux
plt.savefig('./figs/lines/q9.pdf')
plt.savefig('./figs/lines/q9.eps')
#subprocess.run(shlex.split("termux-open ./line/figs/line_check_sol.pdf"))
#else
plt.show()
