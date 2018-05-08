# -*- coding: utf-8 -*-
"""
Created on Mon May  7 22:02:25 2018

@author: singh.shivam
"""
"""
1. create a sample JSON object from titanic train dataset
# https://raw.githubusercontent.com/pcsanwald/kaggle-titanic/master/train.csv
"""

import pandas as pd
Csvfile= pd.read_csv('train.csv')  #open('train.csv','r')
df = pd.DataFrame(Csvfile)

out = df.to_json(orient='columns')
with open('file.json', 'w') as f:
    f.write(out)
# reading the JSON data 
train_phase = pd.read_json('file.json',orient='columns',dtype=True)

HtmlFile = pd.read_html('http://vincentarelbundock.github.io/Rdatasets/datasets.html',skiprows=1)[0]
Html_dataframe = pd.DataFrame(HtmlFile)
Html_dataframe.info()
Html_dataframe1 = Html_dataframe.iloc[:,0:7]
Html_dataframe1.rename(columns=Html_dataframe1.iloc[0],inplace=True)

Html_dataframe=Html_dataframe1.drop([0],axis=0).head() 
Html_dataframe.head()
## Create URL to JSON file (alternatively this can be a filepath)
#url = 'https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/data.json'
# Load the first sheet of the JSON file into a data frame
df = pd.read_json('url.json', orient='columns')
# View the first ten rows
df.head(10)
