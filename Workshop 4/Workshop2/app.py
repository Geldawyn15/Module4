import os
import pandas as pd 
import numpy as np 
import pickle
import flask
from flask import Flask, render_template, request
app=Flask(__name__)

model_path = 'C:/Users/Utilisateur/Documents/Module3/Workshop4/Workshop2/model.pkl'

@app.route('/')
def index():
    return flask.render_template('index.html')
def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1,4)
    loaded_model = pickle.load(open(model_path,'rb'))
    result = loaded_model.predict(to_predict)
    return result[0]

@app.route('/predict',methods = ['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list=list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        result = ValuePredictor(to_predict_list)
        prediction = str(result)
        return render_template("predict.html",prediction=prediction)

if __name__ == "__main__":
 app.run(debug=True)