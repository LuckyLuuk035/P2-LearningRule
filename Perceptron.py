from __future__ import print_function


class Perceptron:
    def __init__(self, bias=0, w=None):
        self.b = bias
        self.msg = -1
        if w is None:
            w = []
        self.w = w

    def __str__(self):
        return self.msg

    def update(self, d, event):
        y = self.activate(self.w, event) # output
        e = d - y
        dw = 0.1 * e * event

    def activate(self, weights, event):
        self.w = weights
        self.msg = ""
        som = 0
        for i in range(len(self.w)):
            self.msg += "'" + str(event[i]) + "i " + str(self.w[i]) + "w" + "'  "
            som = som + event[i]*self.w[i]

        if som + self.b < 0:
            self.msg += "--->  " + str(0) + "         "
            return 0
        elif som + self.b >= 0:
            self.msg += "--->  " + str(1) + "         "
            return 1
        else:  # in het geval van een error (Maak hier een 'try except' van)
            self.msg += "  x   " + str(-1) + "        "
            return -1
