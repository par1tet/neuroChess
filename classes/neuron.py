import numpy as np

def relu(n):
    return max(0, n)

class Neuron:
    def __init__(self, n_inputs):
        self.weights = np.random.randn(n_inputs) * 10 - 5
        self.bias = np.random.randn() * 2 - 1

    def activate(self, inp):
        return relu(np.dot(inp * self.weigth) + self.bias)

    def setValue(self, newValue):
        self.value = newValue

    def getValue(self):
        return self.value