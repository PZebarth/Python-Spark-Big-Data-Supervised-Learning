# Spark Supervised Learning for Customer Churn
# Project Definition
## Project Overview
The data I will be analyzing is from a fictitious company called Sparkify. It works similarly to Spotify. It is a subscription-based music service with two tiers of users, free and premium plan. Users can upgrade from free or downgrade from premium at any time and may also cancel their service all together. <br>

[Customer Churn](https://www.investopedia.com/terms/c/churnrate.asp) is a metric which measures the rate at which customers stop doing business with an entity. In our case when customers move from Sparkify's paid service level to free.<br>

Predicting churn rates is a challenging and common problem that data scientists and analysts regularly encounter in any customer-facing business. Additionally, the ability to efficiently manipulate large datasets with Spark is one of the highest-demand skills in the field of data.<br>

## Problem Statement
The Sparkify data has 18 columns and 286500 rows in the 128MB small dataset. The small dataset is being used to conduct analysis before moving to a 12GB dataset hosted on AWS S3. Using AWS EMR we can use a distributed spark cluster to analyze customer churn. However, first analysis must be conducted on the smaller dataset so we can decide how we are going to label and identify customer churn. <br>

Identifying customer churn is a complex problem. With 18 features in the dataset we need to eliminate ones that won't help identify customer churn through statistical exploratory data analysis. The dataset includes all daily activity, every time a user action changes between songs or pages their data is recorded. We need to change the granularity of the data to effectively use machine learning to identify customer churn. By aggregating features to daily values, we have the opportunity of identifying customer churn daily. For this reason aggregating on daily values is better than weekly or monthly. <br>

For modelling customer churn, we need an appropriate binary classifying machine learning algorithm. This leaves us with the following which I will test: random forest classifier, gradient boosted tree classifier, linear support vector classifier, logistic regression, and a decision tree classifier. The data must be split into testing and validation sets so we can evaluate the effectiveness of our model to identify customer churn. <br>

## Metrics

The dataset is unbalanced with 225 active users and only 52 who churn. When splitting the original data into testing and validation sets the number of users who churn will decrease and still be unbalanced. If we chose to use accuracy as our metric for optimizing our machine learning model we may obtain overfitting the model. In theory it could just predict every user doesn't churn and still maintain a high accuracy score. <br>

We need to use a metric that accounts for correct and incorrect classification better than accuracy. F1 Score does precisely this. We need to evaluate and optimize our chosen model using F1 score to avoid overfitting. This will provide reliable results on the performance of our model. The formula for F1 score is:<br>

$F1 = \frac{2*Precision*Recall}{Precision+Recall}$ <br>

# Methodology
To make a scalable solution the project is broken down into three stages:<br>

>1. Exploratory Data Analysis
>2. Feature Engineering and Scaling
>3. Modelling

## Data Preprocessing
I made use of sparks declarative and imperative programming in steps 1 and 2. I explored all variables and found 4 necessary to engineer the remaining variables. <br>

## Implementation
Identifying customer churn is a complex problem. With 18 features in the dataset we need to eliminate ones that won't help identify customer churn through statistical exploratory data analysis. The dataset includes all daily activity, every time a user action changes between songs or pages their data is recorded. We need to change the granularity of the data to effectively use machine learning to identify customer churn. By aggregating features to daily values we have the opportunity of identifying customer churn daily. For this reason aggregating on daily values is better than weekly or monthly. I scaled them to appropriate dimensions using a min max scaler before proceeding to the modelling step. <br>

## Refinement
The data must be split into testing and validation sets so we can evaluate the effectiveness of our model to identify customer churn. For modelling customer churn we need an appropriate binary classifying machine learning algorithm as well. This leaves us with the following which I will test: 

* random forest classifier <br>
* gradient boosted tree classifier <br>
* linear support vector classifier <br>
* logistic regression <br>
* decision tree classifier <br>

The random forest classifier had the best F1 score and training time on the test data. I hyper tuned the parameters of the random forest classifier to achieve the best model and tested it on the validation set achieving a F1 score of 67-72%.

# Results
## Model Evaluation and Validation
I hyper tuned the parameters of the random forest classifier which were the best of the 5 binary classifiers I tested against the testing data for F1 score and training time. I used a random forest classifier with 10 trees and a max depth of 3 as the grid search cross validation revealed when optimized for F1 score. I tested this model against the validation data and achieved an F1 score of 72% confirming we have improved and tested the preferred model. <br>

## Justification
Due to the unbalanced nature of the dataset with 225 active users and 52 who churned the ensemble of weak learners performed best. The random forest classifier is an ensemble of decision trees, 10 with my model, that average their results and make a prediction. This prevented overfitting due to the unbalanced dataset. The other models are not ensembles and try to fit the data with only one model. <br>

# File Description
The files seen here encompass all my work for this project. There is a separate folder for the web app called "app" which displays visuals and data from Sparkify.ipynb notebook. The notebook contains all the analysis and findings for this project. The file descriptions follow:

>* **Sparkify.ipynb**: detailed analysis report <br>
>* **mini_event_data.json**: subset of data for use in Sparkify.ipynb for creating scalable solution for Spark cluster on AWS<br>

App Folder<br>

>* **run.py**: creates flask app to display webpage<br>
>* **sparkify_data.csv**: original json data converted to csv for display in web app<br>
>* **cleaned_data.csv**: cleaned json data converted to csv for display in web app<br>
>* **feat_eng_data.csv**: feature engineered variables stored in csv for display in web app<br>
>* **plot_1_data.csv**: page interaction data for free and paid subscriptions for display in web app<br>
>* **plot_2_data.csv**: page interaction data for cancelled/churned and active users<br>

App-> templates folder<br>

>* **master.html**: main page of web app <br>
>* **featureengineering.html** feature engineering page of web app<br>
>* **analysis.html** analysis page of web app<br>
>* **results.html** results page of web app<br>

# Running Web App
Make sure the files are downloaded and saved in a folders following the described file description in this README.md file above. 

1. From the command line in the app folder directory enter: **python run.py**
2. From your browser visit: **http://127.0.0.1:3001/**

The web app will load with various visualizations, explore the web app tabs for more data and visualizations.

# Library Dependencies

* Pandas
* Numpy 
* PySpark
* Datetime
* Time
* Plotly
* Flask
* Json

# Final Results

I was able to make several conclusion based on my analysis: <br>

* Page interactions constituted most of my engineered variables and had the greatest covariance with customer churn<br>
* The algorithm had an F1 score and accuracy of 67-72% based on the number of engineered features for the testing data<br>
* This algorithm can scale to a distributed spark cluster to run a 12GB dataset through AWS which is the ultimate goal of this project<br>

In conclusion I made a model which would improve how Sparkify identifies users who will churn and can incentivize them to stay before they leave. <br>

# Conclusion 

The goal of this project is to take a dataset, perform feature engineering, scale the features and perform some modelling so that we can make accurate predictions on whether a customer will churn or not. <br>

This was accomplished through imperative feature engineering of the userId, page, level, and churn columns. Minmax feature scaling was applied to all engineered features. During modelling a random forest classifier was used. I was able to make a model with an f1 of 67-72%% on testing and validation datasets. <br>

Feature engineering had its difficulties. Choosing which features of the original data we wanted to keep and transform to the variables we would use for modelling took a lot of trial and error. What you see in the feature engineering section is my final polished work. I challenged myself to refrain from using SQL or declarative programming, which I'm more comfortable with, and used imperative programming to make it more concise and clean. <br>

I could further improve the exploratory data analysis section which could be made more concise by the use of imperative programming instead of declarative. Furthermore, I wish I choose more parameters to hyper tune to create a model with a better F1 score. After all, the more accurate the model the more users we can retain. <br>
