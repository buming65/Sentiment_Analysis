# Twitter Geospatial Sentiment_Analysis

## Introduction

This project is seperated into 5 stages:
1. Twitter Data Collection
2. Twitte Sentiment Analysis (Naive Bayes)
3. keyword filtering
4. Data Grouping & Centroid Collection
5. Normalization & Visulizaition


Code and data for these stages are stored seven folders: python, stopwords, dataset, result, model, ipynb, script.

Python contains py files of all stages as well as the train and test code of two functions which the files start with 'Analysis' are the codes that use NLTK Naive Bayes Classifier to train our dataset and predict. The files start with 'NaiveBayes' are the codes contain the classifier that was accomplished by ourselves, only use the NLTK package to tokenization, and stemming.

Stopwords contains the stopwords that need to be removed.

Dataset contains the tweets that we collect and data that is outputed from each stage to the next

Result contains the file that each tweet in the dataset has been labeled and it also has the probability of the sentiment as well as the resulting stationary and interative map of visulization.

Model contains the two functions model. One is the model named 'NaiveBayesModel.pickle' which was trained by the NLTK package. The other texts named 'pos_words.txt' and 'neg_words.txt' are the datasets contain the positive words and the negative words that used in our naive bayes classifier.

Ipynb contains ipynb files of all stages and the model evaluations, it also has two file of these two model. The evaluations are the precision, recall, f1, accuracy.

Script contains the script that runs codes from stages

## Run Script 

To run the script, what need to satisfy is that the environment need the python library: sys, csv, nltk, string, re, pickle, math, codecs, pickle, numpy，mapclassify，zipfile，matplotlib，bokeh， eopandas，pysal，requests.

1. Step one:
Here four script: 'Analysis_Test.sh', 'Analysis_Train.sh', 'NaiveBayes_Test.sh', 'NaiveBayes_Train.sh. For this time, we only use the 'data.csv' stored in the dataset folder. All the script are no need to input any parameter. Just run like './Analysis_Test.sh'.

The Analysis_Test.sh predict the 'data.csv' dataset with NLTK classifier.

The Analysis_Train.sh use the Twitter_Sample to train the NLTK classifier.

The NaiveBayes_Test.sh predict the 'data.csv' dataset with the classifier accomplished by ourselves.

The NaiveBayes_Train.sh use the Twitter_Sample to extract the positive words and the negative words.
2. Step Two: Run FurtherFilter.sh
this stage would take the output of sentiment analysis and perform further filtering

3.Step Three: Run 

4. Step Four: Run visulization.sh.
As the final stage, this script would execute the code that takes data outputted from the last stage and create three map as output into the result directory. Specifically, one would be normalized static map, one would be non normalized static map, and one would be interactive map that user can hover to see detail.
