from Perceptron import Perceptron

p1 = Perceptron("INVERT-gate perceptron")
p1.bias = 0.5
p1.weights = [-1]

# print(p1.activate(-1))
# print(p1)

p2 = Perceptron("AND-gate")
p2.bias = -1
p2.weights = [0.5, 0.5]

for i in [[0, 0], [0, 1], [1, 0], [1, 1]]:
    p2.activate(i)
    print(p2)

p3 = Perceptron("OR-gate")
p3.bias = -0.5
p3.weights = [0.6, 0.2]  # were 0.5 0.5


p4 = Perceptron("figuur 2.8")
p4.bias = -0.4
p4.weights = [0.6, 0.3, 0.2]
