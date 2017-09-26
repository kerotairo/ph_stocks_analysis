# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 22:55:26 2017

@author: Kevin Rotairo
"""

import tkinter as tk

from sklearn.externals import joblib

class Application(tk.Frame):
    def __init__(self, model, master=None):
        #Load model
        self.pipeline = joblib.load(model)
        self.sentiment = tk.StringVar()
        super().__init__(master)
        master.title('Sentiment Analyzer')
        master.maxsize(2000, 800)
        master.minsize(400, 100)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.sentiment_label = tk.Label(self, textvariable=self.sentiment)
        self.sentiment_label.pack(side = "bottom")
        
        self.submit = tk.Button(self)
        self.submit["text"] = "Classify!"
        self.submit["command"] = self.change_label
        self.submit.pack(side="bottom")
        
        self.input_label = tk.Label(self)
        self.input_label["text"]= "Enter sentence to analyze:"
        self.input_label.pack(side ="top")
        
        self.sentence_entry = tk.Entry(self)
        self.sentence_entry.pack(side="top")
#        self.quit.pack(side="bottom")

    def change_label(self):
        self.sentiment.set("The given sentence is " +self.get_sentiment(self.sentence_entry.get()))
        self.update()
    
    def get_sentiment(self,sentence):
        return self.pipeline.predict([sentence])[0]
    

model='SentimentAnalyzer_TaggedKeywords.pkl'
root = tk.Tk()
app = Application(model,master=root)
app.mainloop()