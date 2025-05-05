import numpy as np

class Layer:
    def __init__(self, size, inputs):
        self.weigths = np.random.randn(inputs, size) * np.sqrt(2 / inputs)
        self.biases = np.random.randn(size) * 0.1

    def activate(self, prefLayer, activate_type):
        if activate_type == 'relu':
            return np.maximum(0, np.dot(prefLayer, self.weigths) + self.biases)
        elif activate_type == 'sigmoid':
            return 1 / (1 + np.exp(-np.dot(prefLayer, self.weigths) + self.biases))
        elif activate_type == 'tanh':
            return np.tanh(np.dot(prefLayer, self.weigths) + self.biases)