import numpy as np
import matplotlib.pyplot as plot

# Variables

# Zorros
foxes = 10
foxesSurvivalRate = 0.0004
foxesMortalityRate = 0.2

# Liebres
hares = 500
haresGrowth = 0.08
haresLostPerHunt = 0.002

# Terreno y tiempo
terrainCapacity = 1400
weeks = 500

# Listas con el total de Zorros y el total de Liebres en el tiempo dado.
totalHares = list(range(weeks))
totalFoxes = list(range(weeks))

for t in range(weeks):
    actualCapacity = terrainCapacity - hares
    haresRate = (1/terrainCapacity)*actualCapacity*haresGrowth*hares
    foxSurvival = foxesMortalityRate*foxes
    hunt = foxes*hares
    hares = hares+(haresRate-haresLostPerHunt*hunt)
    foxes = foxes+(foxesSurvivalRate*hunt-foxSurvival)
    totalHares[t] = hares
    totalFoxes[t] = foxes

# Gráficas
xTime = np.linspace(0, weeks, weeks)
y1Hares = np.array(totalHares)
y2Foxes = np.array(totalFoxes)

# Variación de poblaciones en el tiempo
plot.plot(xTime, y1Hares, label='Hares')
plot.plot(xTime, y2Foxes, label='Foxes')
plot.xlabel('Tiempo')
plot.ylabel('Predador Presa')                
plot.title('Variación de las poblaciones')
plot.legend()
plot.grid()
plot.show()

# Diagrama de Fases
plot.plot(y1Hares, y2Foxes)
plot.xlabel('Hares')
plot.ylabel('Foxes')
plot.title('Diagrama de fase')
plot.grid()
plot.show()
