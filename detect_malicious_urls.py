# -*- coding: utf-8 -*-
"""Detect Malicious URLs.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hmSxYh5ONhrXsLWoKB17eykQwHbYsYRy
"""

import pandas as pd
import numpy as np
import csv
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
import random
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('./Data/data.csv')
df.head()

print('Before Removing Duplicates')
print('Total : ' , len(df))
print('Good : ' , len(df[df['label'] == 'good']))
print('Bad : ' , len(df[df['label'] == 'bad']))
df.drop_duplicates(subset='url',keep=False,inplace=True)
print('After Removing Duplicates')
df.reset_index(drop=True,inplace=True)
print('Total : ' , len(df))
print('Good : ' , len(df[df['label'] == 'good']))
print('Bad : ' , len(df[df['label'] == 'bad']))

def encode_categorical(df, column_list):
    for column in column_list:
        df[column] = df[column].astype('str')
        encoder = preprocessing.LabelEncoder()
        encoded_list = encoder.fit_transform(df[column])
        encoded_series = pd.Series(encoded_list)
        df[column] = encoded_series
        print("The ", column, "is encoded ")
    return(df)

df = encode_categorical(df, ['label'])

df1 = np.array(df)
random.shuffle(df1)
print(df1)

y = [d[1] for d in df1]
url = [d[0] for d in df1]
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(url)

print(X[0])

x_train,x_test,y_train,y_test=train_test_split(X, y, test_size=0.2,shuffle=True,stratify=y)

from sklearn.linear_model import LogisticRegression
LR = LogisticRegression(random_state=0).fit(x_train, y_train)
accuracy = LR.score(x_test, y_test)
print('Accuracy : ' ,accuracy)

predict = LR.predict(x_test)
conf_mat = confusion_matrix(y_test, predict)
print(conf_mat)
print(classification_report(y_test, predict))

""".  | Bad Predicted | Good Predicted
--- | --- | ---
Bad Actual | 21369 | 1147
Good Actual | 241 | 57874
"""

pickle.dump(LR, open("LR_saved_model.pickle", "wb"))
pickle.dump(vectorizer, open("tfidf.pickle", "wb"))
