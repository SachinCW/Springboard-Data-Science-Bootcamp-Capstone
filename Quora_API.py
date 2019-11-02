# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 13:01:14 2019

@author: sachi
This has the code that loads the model in memory, creates the Flask API and hosts it for it to be ready listening to the requests for prediction
"""

# Dependencies

from Quora_preprocess import preprocess_text
from flask import Flask, request, jsonify
import traceback
import pandas as pd
import pickle

# Your API definition
app = Flask(__name__)



@app.route("/", methods=["GET","POST"])
def predict():
    if load_clf_model:
        
        try:
            json_ = request.json
            Q=[]
            Q.append(dict(json_))
            query = preprocess_text(pd.DataFrame(Q))
          
            pred_proba_df = pd.DataFrame(load_clf_model.predict_proba(query['word_tokens_stemmed']))
            y_pred = pred_proba_df.applymap(lambda x: 1 if x>0.4 else 0)
            prediction=list(y_pred.iloc[:,1].as_matrix().reshape(y_pred.iloc[:,1].as_matrix().size,1))[0][0]
           
            return jsonify({'prediction': str(prediction)})
            
        except:
            print(json_)
            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Train the model first')
        return ('No model here to use')

if __name__ == '__main__':
    filename='quora_classification_model.sav'
    load_clf_model =pickle.load(open(filename, 'rb')) # Load model
    print ('Model loaded')
    

    app.run(debug=True)