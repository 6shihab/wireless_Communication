Tn=150*10**-6 #total Delay Time
N=70  #multipath bins ( multipath Components)
delT=Tn/N  #singlepath bins delay time
maxBW=2/delT
print(delT)
print(maxBW)