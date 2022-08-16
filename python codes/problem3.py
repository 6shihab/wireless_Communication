import math

GOS = 0.005
Au = 0.1  # single user traffic intensity
A = 0.005  # from Erlang B table supported traffic intensity
U = math.ceil(A / Au)  # total number of user per cell
print(U)
