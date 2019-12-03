# Springboard-Capstone Project

An existential problem for any major website today is how to handle toxic and divisive content. Quora wants to tackle this problem head-on to keep their platform a place where users can feel safe sharing their knowledge with the world.

Quora is a platform that empowers people to learn from each other. On Quora, people can ask questions and connect with others who contribute unique insights and quality answers. A key challenge is to weed out insincere questions -- those founded upon false premises, or that intend to make a statement rather than look for helpful answers.

Through this project, I developed models that identify and flag insincere questions. To date, Quora has employed both machine learning and manual review to address this problem. I intended to develop more scalable methods to detect toxic and misleading content.

This is a chance to combat online trolls at scale and help Quora uphold their policy of “Be Nice, Be Respectful” and continue to be a place for sharing and growing the world’s knowledge.

## General Description:

In this project, task was to predict whether a question asked on Quora is sincere or not.

An insincere question is defined as a question intended to make a statement rather than look for helpful answers. Some characteristics that can signify that a question is insincere:

    Has a non-neutral tone
  
      Has an exaggerated tone to underscore a point about a group of people
      Is rhetorical and meant to imply a statement about a group of people
      
    Is disparaging or inflammatory
    
      Suggests a discriminatory idea against a protected class of people, or seeks confirmation of a stereotype
      Makes disparaging attacks/insults against a specific person or group of people
      Based on an outlandish premise about a group of people
      Disparages against a characteristic that is not fixable and not measurable
      
    Isn't grounded in reality
      Based on false information, or contains absurd assumptions
      
    Uses sexual content (incest, bestiality, pedophilia) for shock value, and not to seek genuine answers




## Dataset:
Dataset for this project can be found on the kaggle competition on which this project is based. 
https://www.kaggle.com/c/quora-insincere-questions-classification/data

It has 1.3 million records in the training file which is 118 meg in size. It also has the popular embedding files mentioned below which run into a few giga bytes in size ranging from 2 GB to 6 GB.

1) GoogleNews-vectors-negative300.bin

2) glove.840B.300d.txt

3) paragram_300_sl999.txt

4) wiki-news-300d-1M.vec

The dataset from Kaggle was easily downloaded to the Google Drive account using Kaggle API and then Google drive was mounted in the Google Colab for access to the dataset in the Colab notebooks.

The following article sums up the process pretty well.

https://towardsdatascience.com/setting-up-kaggle-in-google-colab-ebb281b61463

## Approach to solve this problem:
This is a supervised classification problem in which the question_text data field will be used as a predictor and the target data field has a value of 1 and 0 that indicate whether the question is insincere or not respectively.

This is a classic NLP based project on which traditional machine learning algorithms, as well as Deep Learning, can be applied. I applied both traditional and Deep Learning Methodologies in this project.

## Computational Resources Utilized:
I needed access to GPU for applying Deep Learning Techniques for which I used Google Colab.
I also found that I needed 25 Gig Ram while which again was found through Google Colab.

## Final Deliverable:
An application deployed as a web service with an API.


## Information about the files in this project:

Quora_Experiments_using_Vanilla_Algorithms.ipynb : This is a notebook of the Data Science Experiments conducted on the dataset using Vanilla ML Algorithms.

Quora_Quest_Use_Pretrained_Embeddings.ipynb : This is an Experiment using pre trained word embeddings obtained by Gensim's word2vec implementation.

Quora_Quest_Build_Embeddings_using_word2vec.ipynb : This is an experiment training word2vec on the dataset to build our own embeddings or simply put word vectors using the Gensim implementation of Word2Vec.

Quora_CNN.ipynb : This is an experiment using Convolutional Neural Network.

Quora_LSTM.ipynb : This is an experiment using LSTM (Long Short Term Memory ) Neural Network.

Quora_Final_Model_Training_Notebook.ipynb : This is the finalised model training notebook. The model is dumped into a file in this notebook.

Quora_API.py : This python file has the code to load the model in memory, create the Flask API and host the API for it to be ready listening to the requests for prediction. It listens to the request and performs prediction and returns the prediction requested.

Quora_preprocess.py : This python file has the definitions for preprocessing the questions posted by the requests for prediction.

contraction_map.py : This python file hosts the dictionary of contractions used in the preprocessing step.

quora_request.py : This python file sends the request to the Flask API that contains the question to be classified as Sincere vs Insincere
