import math
#given
f=900*10**6
c=3*10**8
lamda=c/f
D=1
fraunhoferDistance_d=2*D**2/lamda
print(fraunhoferDistance_d)
path_loss=-10*math.log((lamda/(4*3.1416*fraunhoferDistance_d))**2,10)
print(path_loss)