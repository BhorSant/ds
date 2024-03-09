from flask import Flask, render_template,request
import os
import numpy as np
import pandas as pd
from mlProject.pipeline.prediction import PredictionPipeline


app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def index():
    if request.method == 'POST':
        try:
            data = request.form['data']
            pred = PredictionPipeline()
            results = pred.predict([np.array(list(data.values()))])

            return render_template('index.html',results = results[0])
        except Exception as e:
            print(e)
            return 'something is wrong'
    else:
        return render_template('index.html',results = None, results2 = None)
    
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000)
    
    
                            