import math

GOS = 2 / 100

Au = (2 * 3) / 60  # single user traffic intensity
A = 12  # from Erlang B table supported traffic intensity
U = math.ceil(A / Au)  # total number of user per cell
totalSubscriber = 394 * U
print(U)
print(totalSubscriber)
print("Market Penetration: ", "{:0.2f}".format((totalSubscriber / (2 * 10 ** 6)) * 100), "%")
