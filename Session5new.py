# -*- coding: utf-8 -*-
"""
Created on Mon May  7 22:02:25 2018

@author: singh.shivam
"""
"""
1. create a sample JSON object from titanic train dataset
# https://raw.githubusercontent.com/pcsanwald/kaggle-titanic/master/train.csv
"""
import csv
import json 
import pandas as pd
Csvfile= pd.read_csv('train.csv')  #open('train.csv','r')
df = pd.DataFrame(Csvfile)

jsonfile = open('file.json', 'w')

fileHeader =df.columns
reader = csv.DictReader( Csvfile,fileHeader)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')

   
# reading the JSON data using json.load()
#file ='file.json'
with open('file.json') as train_file:
    dict_train = json.load(train_file)

# converting json dataset from dictionary to dataframe
train = pd.DataFrame.from_dict(dict_train, orient='index')
train.reset_index(level=0, inplace=True) 

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
df = pd.read_json('url.csv', orient='columns')
# View the first ten rows
df.head(10)