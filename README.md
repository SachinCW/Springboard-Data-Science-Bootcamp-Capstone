# Springboard-Capstone
-- This readme file will be updated pretty soon. --

Information about the files in this project:

Quora_Experiments_using_Vanilla_Algorithms.ipynb : This is a notebook of the Data Science Experiments conducted on the dataset using Vanilla ML Algorithms.

Quora_Final_Model_Training_Notebook.ipynb : This is the finalised model training notebook. The model is dumped into a file in this notebook.

Quora_API.py : This python file has the code to load the model in memory, create the Flask API and host the API for it to be ready listening to the requests for prediction. It listens to the request and performs prediction and returns the prediction requested.

Quora_preprocess.py : This python file has the definitions for preprocessing the questions posted by the requests for prediction.

contraction_map.py : This python file hosts the dictionary of contractions used in the preprocessing step.

quora_request.py : This python file sends the request to the Flask API that contains the question to be classified as Sincere vs Insincere
