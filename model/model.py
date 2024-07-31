import matplotlib.pyplot as plt
import numpy as np
import json
from threading import Thread

class Predict:
    def __init__(self, x) -> None:
        self.x = x
        self.W = self.open_file()
        self.W = np.array(self.W)
        
    def open_file(self):
        with open("D:\Engineering\Build Model\data\poids.json",'r') as file:
            data = json.load(file)
            file.close()
        return data
    
    def predict(self):
        return self.W.dot(self.x)

class Neural_Network:
    def __init__(self,x, y, epoch , learning_rate : float = 0.01, nb_input : int = 1, layers : int = 1) -> None:
        print(x, y, epoch, learning_rate, nb_input, layers)
        self.W      = np.random.randn(int(layers), int(nb_input))
        self.b      = np.zeros((1, int(nb_input)))
        self.x      = x
        self.y      = y
        self.epoch  = epoch
        self.lr     = learning_rate
        self.loss   = []
        self.layers   = layers
        self.nb_input = nb_input

    def gradual_approach(self, a, b, W) -> float:  
        return W - self.lr if a > b else W + self.lr if a < b else W
    
    def add_layer(self, inp, layer):
        return self.W[layer - 1].dot(inp)
        
    def model(self, x : int or float) -> float:
        activations = {}
        for layer in range(1, self.layers + 1):
            if layer == 1:
                activations[f"A{layer}"] = self.add_layer(x, layer)     
            else : 
                temp = self.add_layer(activations[f"A{layer - 1}"], layer)
                activations[f"A{layer}"] = temp[-1]
            
        return activations
    
    def update(self, out : float, i : int) -> None:
        for layer in range(1, self.layers + 1):
            for w in range(self.nb_input):
                self.W[layer-1][w] = self.gradual_approach(out[f"A{layer}"], self.y[i], self.W[layer-1][w])
        self.loss.append(self.y[i] - out[f"A{self.layers}"])
        
    def predict(self) -> None:  
        while True:
            pred = []
            for i in range(self.nb_input):
                pred.append(int(input("X" + str(i+1) + " : ")))
            print(self.model(np.array(pred)))
            
    def draw(self):
        plt.plot(self.loss)
        plt.show()
        
    def save_weight(self):
        with open("D:\Engineering\Build Model\data\poids.json",'w') as file:
            json.dump(self.W.tolist(), file, indent=4)
            file.close()
        
    def amorce(self) -> None:
        indice = 0
        for i in range(self.epoch):
            if indice == len(self.x) - 1:
                indice = 0
            out = self.model(self.x[indice])
            out = self.update(out, indice)
            print("Epoch : " ,i, "/", self.epoch, "| Loss : ", self.loss[-1])

            indice += 1
            
        print(self.W)
        self.save_weight()

        if __name__ == "__main__":
            thread_draw = Thread(target = lambda : self.draw())
            thread_draw.start()
            #self.predict()
            del thread_draw

            
if __name__ == "__main__":
    def load_trainset():
        file = open("trainset.json", 'r')
        data = json.load(file)
        x = data['x']
        y = data['y']
        return (x,y)
    x = [1,2,3,4,5,6,7,8,9,10]
    y = [200, 400, 500, 700, 900, 1000, 1200, 1400, 1500, 1700]    

    x = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    y = [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50]   
    x = [2,4,6,8,10]
    y = [1,2,3,4,5] 



    x = [1,2,3,4,5,6,7,8,9,10]
    y = [200, 400, 500, 700, 900, 1000, 1200, 1400, 1500, 1700]    
    x = [[1,0],[2, 0],[3,0],[4,0],[5,0],[6, 0],[7, 0],[8, 0],[9, 0],[10,0],
         [1,1],[2, 1],[3,1],[4,1],[5,1],[6, 1],[7, 1],[8, 1],[9, 1],[10,1]]
    y = [200, 400, 500, 700, 900, 1000, 1200, 1400, 1500, 1700,
         100, 300, 400, 600, 800, 900, 1100, 1300, 1400, 1600]    
    
    x = [
        [1,2,3,4] ,[2,3,4,5], [6,6,6,6], [5,5,5,5], [2,3,7,9], [2,1,5,8], [10,2,5,22], [23,1,4,2]
    ]
    
    y = [10, 14, 24, 20, 21, 16, 39, 30 ]
    
    x = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    y = [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50]   
    #x, y = load_trainset()
    iter = 5000
    learning_rate = 0.01
    nb_input = 1
    model = Neural_Network(x, y, iter, learning_rate, nb_input)
    model.amorce()