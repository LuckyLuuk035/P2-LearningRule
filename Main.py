from Perceptron import Perceptron
import random


p1 = Perceptron("AND-gate")
p1.bias = random.uniform(-1, 1)
p1.w = [random.uniform(-1, 1), random.uniform(-1, 1)]

p2 = Perceptron("XOR-gate")
p2.bias = random.uniform(-1, 1)
p2.w = [random.uniform(-1, 1), random.uniform(-1, 1)]

print("AND-gate")
p1.update([[0, [0, 0]], [0, [0, 1]], [0, [1, 0]], [1, [1, 1]]], 30, 0.2)

print("XOR-gate")
p2.update([[0, [0, 0]], [1, [0, 1]], [1, [1, 0]], [0, [1, 1]]], 200, 0.3)
# Deze is niet mogelijk doordat een perceptron alleen maar lineare verdeelbare data kan leren.
# als je een grafiek ziet zou je met 1 streep de 0 en 1 kunnen splitsen.
