# given
# m (t) = 8cos(2pi*4 x 10^3*t+10)
A=8
f=4*10**3
k=10*10**3
peak_frequency_deviation=A*k
print(peak_frequency_deviation)
modulation_index=peak_frequency_deviation/f
print(modulation_index)
print("Phase Modulation Index",A*10, "radians")