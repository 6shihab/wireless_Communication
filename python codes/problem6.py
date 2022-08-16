# given
carrierFrequency = 900 * 10 ** 6
valocity = (70 * 1000) / 3600
print(valocity)
c = 3 * 10 ** 8
lamda = c / carrierFrequency
# v=f*lamda
# for moving forward to the transmitter
recvfreqMF = carrierFrequency + valocity / lamda
print("{:0.2f}".format(recvfreqMF / (10 ** 6)), "MHz")
directlyAway = carrierFrequency - valocity / lamda
print("{:0.4f}".format(directlyAway / (10 ** 6)), "MHz")
