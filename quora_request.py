# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 15:51:21 2019

@author: sachi

This python file posts a request for the Flask API using the Quora question that we want to know if it's sincere or insincere.

"""

import requests

url = 'http://localhost:5000/'
r = requests.post(url,json={"question_text":"If blacks support school choice and mandatory sentencing for criminals why don't they vote Republican?"})

print(r.json())