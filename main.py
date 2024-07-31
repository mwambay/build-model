from flask import Flask, render_template, request, jsonify
import sys
import os
chemin_parent = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
chemin_parent = r"D:\Engineering\BUILD MODEL"
sys.path.append(chemin_parent)
from model.model import Neural_Network
from model.model import Predict

def amorce_model(X, Y, nb_input, layers, epoch, learning_rate):
    print("Parameters : ", nb_input, layers, epoch, learning_rate)
    model = Neural_Network(X, Y, int(epoch), learning_rate, int(nb_input), int(layers) )
    model.amorce()
    print("finish")
    return {"verdict" : 1 }
app = Flask(__name__)

@app.route('/executer_code', methods=['GET', 'POST'])
def executer_code():
    if request.method == 'POST':
        X = request.form.get('input')
        X = float(X)
        model = Predict(X)
        model = model.predict()
        print(model)
        data = {"prediction" : model.tolist()}
        return jsonify(result=data)


@app.route('/', methods=['GET', 'POST'])
def index():
    
    def format_input(a):
        temp = []
        text = ''
        for index, i in enumerate(a):
            if i == ',': 
                temp.append([int(text)])
                text=''
            else: text += i
            
            if index == len(a) - 1 : temp.append([int(text)])
        return temp
    
    def format_output(a):
        temp = []
        text = ''
        for index, i in enumerate(a):
            if i == ',': 
                temp.append(int(text))
                text=''
            else: text += i
            
            if index == len(a) - 1 : temp.append(int(text))
        return temp
    
    if request.method == 'POST':
        try:
            X = request.form.get('inputs')
            X = format_output(X)
            print("X: ", X)
            Y = request.form.get('outputs')
            Y = format_output(Y)
            layers = request.form.get('layers')
            nbNeuron = request.form.get('nbNeuron')
            learning_rate = request.form.get('Learning_rate')
            learning_rate = float(learning_rate)
            learning_rate /= 100
            epoch = request.form.get("iter")
            print("y : ", Y)
            print("layers : ", layers)
            print("neuronne : ", nbNeuron)
            print("learnig : ", learning_rate)
            print("epoch: ", epoch)
            data = amorce_model(X, Y, int(nbNeuron), int(layers),int(epoch), float(learning_rate))

            return jsonify(result=data)  # Retourne le résultat sous forme JSON
        except:
            data = {"verdict" : 0 }
            return jsonify(result=data)
    return render_template('build.html')

if __name__ == '__main__':
    app.run()
