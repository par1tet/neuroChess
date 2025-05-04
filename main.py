import numpy
from classes.model import Model

model = Model(64, [64, 32, 16, 1])

#print(layer.getLayer())

table = []

for i in range(64):
    randFig = numpy.random.randint(0,7)
    fig = 0
    if randFig == 1:
        fig = 1
    elif randFig == 2:
        fig = 3
    elif randFig == 3:
        fig = 4
    elif randFig == 4:
        fig = 5
    elif randFig == 5:
        fig = 9
    elif randFig == 6:
        fig = 10
    table.append(fig / 10)

print(model.getRes(table))