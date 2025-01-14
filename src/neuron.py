import math
class Neuron:
    def __init__(self, weights, bias, func):
        self.weights = weights
        self.bias = bias
        self.func = func
    
    def __sigmoide(z):
        return 1 / 1 + (math.exp(-z))
    
    def __tanh(z):
        return (math.exp(z) - math.exp(-z)) / (math.exp(z) + math.exp(-z))
    
    def __relu(z):
        return max(0, z)
    
    def __binary_step(z):
        return 1 if z >= 0 else 0
    
    def changeBias(self, bias):
        self.bias = bias
    
    def changeWeights(self, weights):
        self.weights = weights
    
    def run(self, input_data):
        if len(self.weights) != len(input_data):
            return "ERROR: El número de pesos es diferente al numero de entradas"
        else:
            if self.func == "sigmoide":
                return Neuron.__sigmoide(sum(x * w for x, w in zip(input_data, self.weights)) + self.bias)
            elif self.func == "tanh":
                return Neuron.__tanh(sum(x * w for x, w in zip(input_data, self.weights)) + self.bias)
            elif self.func == "relu":
                return Neuron.__relu(sum(x * w for x, w in zip(input_data, self.weights)) + self.bias)
            elif self.func == "binary_step":
                return Neuron.__binary_step(sum(x * w for x, w in zip(input_data, self.weights)) + self.bias)
            else:
                return "ERROR: Esa función no existe o no está disponible"