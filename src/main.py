"""
A simple RL agent that plays the pong game to perfection. This implementation is based on policy gradients.
"""
import numpy as np

def test(input, weight_matrix, weight_vector):
    # Getting the layer1 output
    layer1 = np.dot(weight_matrix, input)

    # RELU for getting consistent values
    # TODO
    layer1[h < 0] = 0

    # Getting the layer2 output
    layer2 = np.dot(weight_vector, layer1)

    # Sigmoid for squashing into a probability range [0,1]
    output_probability = 1.0 / (1.0 + np.exp(layer2))
