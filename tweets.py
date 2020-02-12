#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 19:38:32 2020

@author: P Jakobsen
Thanks for Pandas help to
data set is from https://www.kaggle.com/kazanova/sentiment140
#This guy already did the work
https://www.kaggle.com/mistryjimit26/twitter-sentiment-analysis-basic/code
#And more recently
https://www.kaggle.com/udipta/starter-sentiment140-dataset-with-1-6-b64b1db5-e/notebook

"""
import pandas as pd
import numpy as np

import sys
tweet_df= pd.DataFrame()
def preload(file,encoding,header=None):
    #import data from csv file via pandas library
    #tweet_dataset = pd.read_csv(filename, encoding = 'utf-8', header = header)

    df = pd.read_csv(file,encoding,header,engine = 'python',delimiter=',')
    print(df.info())
    #the column names are based on sentiment140 dataset provided on kaggle
    df.columns = ['sentiment','id','date','flag','user','text']
    print(df.info())
    #delete flags,id,user, date
    #df=df.drop(["id","user","date","user"], axis = 1)

    #in sentiment140 dataset, positive = 4, negative = 0; So we change positive to 1
    #df.sentiment = df.sentiment.replace(4,1)
    #df.to_pickle('data/tweets.pkl')
    #return df

    # Drop irrelevant columns
    #tweet_df = tweet_df.drop(tweet_df.columns[[13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39]], axis=1)

#preload('data/training.1600000.processed.noemoticon.csv','latin-1',None)

df = pd.read_csv('data/cleaned.csv', delimiter=',',
                  nrows = 1600000)
print(df.tail())
sys.exit()

#df = pd.read_pickle('data/tweets.pkl')
#
#print(df.info())
#
#data = np.array(df.text)
#label = np.array(df.sentiment)


#print(df.head())
