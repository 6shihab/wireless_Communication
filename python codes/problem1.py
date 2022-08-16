totalBW = 30 * 10 ** 6
channelBW = 2 * 25 * 10 ** 3
conChaBW = 1 * 10 ** 6
totalChannel = totalBW / channelBW
totalConCha = conChaBW / channelBW
totalVoiceChannel = totalChannel - totalConCha

# for n=4
numVoice = int(totalVoiceChannel / 4)
numCon = totalConCha / 4
print("n=4 \nTotal channel = ", totalChannel / 4)
print("Number Of voice channel =", numVoice)
print("Number Of Control Channel = ", numCon)
