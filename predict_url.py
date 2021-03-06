# -*- coding: utf-8 -*-
"""predict_url.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bXMSL1z4pD2d0IkUnyojQZbAmLBVzQqQ
"""

import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

def predict(url):
  LR = pickle.load(open('LR_saved_model.pickle','rb'))
  vectorizer = pickle.load(open('tfidf.pickle','rb'))
  url = vectorizer.transform([url])
  result = LR.predict(url)
  result = result[0]
  return result