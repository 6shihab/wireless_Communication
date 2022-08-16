modulatedPower_Pam=400*10**3
modulationIndex_k=0.75
carrierpower_Pc=modulatedPower_Pam/(1+(modulationIndex_k**2)/2)
print(carrierpower_Pc)
print("Percentage in power",(carrierpower_Pc/modulatedPower_Pam)*100,"%")
power_in_each_Sideband_Ps=0.5*(modulatedPower_Pam-carrierpower_Pc)
print(power_in_each_Sideband_Ps)
ps=(modulatedPower_Pam-power_in_each_Sideband_Ps)*100/modulatedPower_Pam  #percentage power saving if one of sideband carrier is suppressed

print(ps)