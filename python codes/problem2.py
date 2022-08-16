import math

# for n=4
# let assume N=7
N = 7
n = 4
i = 6
signalInterfracnceRatio = (math.sqrt(3 * N) ** n) / 6
signalIRdB = 10 * math.log(signalInterfracnceRatio, 10)
print(signalIRdB)
