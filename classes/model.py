from classes.layer import Layer

class Model:
    layers = []

    def __init__(self, input, layers):
        for n in range(len(layers)):
            if n == 0:
                self.layers.append(Layer(layers[n], input))
            else:
                self.layers.append(Layer(layers[n], layers[n-1]))

    def getRes(self, input):
        prefForward = input

        for i in range(len(self.layers)):
            if i != len(self.layers) - 1:
                prefForward = self.layers[i].activate(prefForward, "sigmoid")
                continue

            prefForward = self.layers[i].activate(prefForward, "sigmoid")

        return prefForward