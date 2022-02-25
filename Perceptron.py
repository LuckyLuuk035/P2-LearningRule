from __future__ import print_function


class Perceptron:
    def __init__(self, name, w=None):
        self.name = name
        self.b = 0
        self.msg = -1
        if w is None:
            w = []
        self.w = w

    def __str__(self):
        return self.msg

    def update(self, truthtable, epochs=5):
        count = 0
        target = []
        input = []
        for i in truthtable:
            target.append(i[0])
            input.append(i[1])
        
        for i in range(len(target)):
            while count <= epochs:
                d = target[i]
                x = input[i]
                y = self.activate(x)  # output
                print(self)
                e = d - y

                for j in range(len(self.w)):
                    self.w[j] += 0.1 * e * y

                db = 0.1 * e
                self.b += db
                count += 1
            count = 0
            print(x, "done.  Predicted output should be:", d)

    def activate(self, event):
        self.msg = ""
        som = 0
        for i in range(len(self.w)):
            self.msg += "'" + str(event[i]) + "i " + str(self.w[i]) + "w" + "'  "
            som = som + event[i]*self.w[i]
        self.msg += str(self.b) + "b  "
        if float(som) + float(self.b) < 0:
            self.msg += "--->  " + str(0) + "         "
            return 0
        elif float(som) + float(self.b) >= 0:
            self.msg += "--->  " + str(1) + "         "
            return 1
        else:  # in het geval van een error (Maak hier een 'try except' van)
            self.msg += "  x   " + str(-1) + "        "
            return -1
