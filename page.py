from tkinter import *
from predict_url import predict
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

page = Tk()
page.geometry("500x400")
page.title("CHECK URL")


strr = StringVar()

def check():
    str = strr.get()
    c = predict(str)
    if(c == 0):
        lable1 = Label(page, text="THE PAGE IS MALICIOUS", fg="red", font=("arial", 15, "bold"))
        lable1.place(x=120, y=280)
    elif(c == 1):
        lable2 = Label(page, text="THIS PAGE IS SAFE,YOU ARE GOOD TO GO!!", fg="blue", font=("arial", 15, "bold"))
        lable2.place(x=30, y=280)
        
    
    

lable = Label(page, text="Enter URL", font=("arial", 22, "bold"))
lable.place(x=180, y=100)

entry = Entry(page, textvar=strr, width=35, font=("arial", 16))
entry.place(x=40, y=150)

button=Button(page, text="SUBMIT", fg="white", bg="red", relief=RAISED, font=("arial", 14, "bold"), command=check)
button.place(x=200, y=200)

page.mainloop()
