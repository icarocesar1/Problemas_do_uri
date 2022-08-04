entradaTempo = int(input())


horaTempo = entradaTempo//3600
minutoTempo = entradaTempo % 3600 // 60
segundoTempo = int(entradaTempo % 60)

print("%i:%i:%i" %(horaTempo, minutoTempo, segundoTempo))
