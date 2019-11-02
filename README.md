# Springboard-Capstone
-- This readme file will be updated pretty soon. --

# Dataset:
Dataset for this project can be found on the kaggle competition on which this project is based. 
https://www.kaggle.com/c/quora-insincere-questions-classification/data

It has 1.3 million records in the training file which is 118 meg in size. It also has the popular embedding files mentioned below which run into a few giga bytes in size ranging from 2 GB to 6 GB.

GoogleNews-vectors-negative300.bin
glove.840B.300d.txt
paragram_300_sl999.txt
wiki-news-300d-1M.vec

The dataset from Kaggle was easily downloaded to the Google Drive account using Kaggle API and then Google drive was mounted in the Google Colab for access to the dataset in the Colab notebooks.

The following article sums up the process pretty well.
https://towardsdatascience.com/setting-up-kaggle-in-google-colab-ebb281b61463



# Information about the files in this project:

Quora_Experiments_using_Vanilla_Algorithms.ipynb : This is a notebook of the Data Science Experiments conducted on the dataset using Vanilla ML Algorithms.

Quora_Final_Model_Training_Notebook.ipynb : This is the finalised model training notebook. The model is dumped into a file in this notebook.

Quora_API.py : This python file has the code to load the model in memory, create the Flask API and host the API for it to be ready listening to the requests for prediction. It listens to the request and performs prediction and returns the prediction requested.

Quora_preprocess.py : This python file has the definitions for preprocessing the questions posted by the requests for prediction.

contraction_map.py : This python file hosts the dictionary of contractions used in the preprocessing step.

quora_request.py : This python file sends the request to the Flask API that contains the question to be classified as Sincere vs Insincere
