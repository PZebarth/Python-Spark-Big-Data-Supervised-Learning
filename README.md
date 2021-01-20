# Spark Supervised Learning for Customer Churn
## Project Overview
The data I will be analyzing is from a fictious company called Sparkify. It works similarily to Spotify. It is a subscription based music service with two tiers of users, free and premium plan. Users can upgrade from free or downgrade from premium at any time and may aslo cancel their service all together.<br>

[Customer Churn](https://www.investopedia.com/terms/c/churnrate.asp) is a metric which measures the rate at which customers stop doing business with an entity. In our case when customers move from Sparkify's paid service level to free.<br>

Predicting churn rates is a challenging and common problem that data scientists and analysts regularly encounter in any customer-facing business. Additionally, the ability to efficiently manipulate large datasets with Spark is one of the highest-demand skills in the field of data.<br>

## Problem Statement
The sparkify data has 18 columns and 286500 rows in the 128MB small dataset. The small dataset is being used to conduct analysis before moving to a 12GB dataset hosted on AWS S3. Using AWS EMR we can use a distributed spark cluster to analyze customer churn. However, first analysis must be conducted on the smaller dataset so we can decide how we are going to label and identify customer churn.<br>

Identifying customer churn is a complex problem. With 18 features in the dataset we need to eliminate ones that won't help identify customer churn through statistical exploratory data analysis. The dataset includes all daily activity, everytime a user action changes between songs or pages their data is recorded. We need to change the granularity of the data for it to effectively use machine learning to identify customer churn. By aggregating features to daily values we have the opportunity of identifying customer churn daily. For this reason aggregating on daily values is better than weekly or monthly.<br>

For modelling customer churn we need an appropriate binary classifying machine learning algorithm. This leaves us with the following which I will test: random forest classifier, gradient boosted tree classifier, linear support vector classifier, logistic regression, and a decision tree classifier. The data must be split into testing and validation sets so we can evaluate the effectiveness of our model to identify customer churn.<br>

## Metrics

The dataset is unbalanced with 225 active users and only 52 who churn. When splitting the original data into testing and validation sets the number of users who churn will decrease and still be unbalanced. If we chose to use accuracy as our metric for optimizing our machine learning model we may obtain overfitting the model. In theory it could just predict every user doesn't churn and still maintain a high accuracy score.<br>

We need to use a metric that accounts for correct and incorrect classification better than accuracy. F1 Score does precisley this. We need to evaluate and optimize our chosen model using F1 score to avoid overfitting. This will provide reliable results on the operformance of our model. The formula for F1 score is:<br>

$F1 = \frac{2*Precision*Recall}{Precision+Recall}$<br>

## Project Description
To make a scalable solution the project is broken down into three stages:<br>

>1. Exploratory Data Analysis
>2. Feature Engineering and Scaling
>3. Modelling

I made use of sparks declarative and imperative programming in steps 1 and 2. I explored all variables and found 4 neccessary to engineer the remaining variables. I scaled them to appropriate dimensions. Then I modelled the data using several machine learning algorithms from which I chose one with the best metrics and performance so my solution could scale.

## File Description
The files seen here encompass all my work for this project. There is a seperate folder for the web app called "app" which displays visuals and data from Sparkify.ipynb notebook. The notebook contains all the analysis and findings for this project. The file descriptions follow:

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

## Running Web App
Make sure the files are downloaded and saved in a folders following the described file description in this README.md file above. 

1. From the command line in the app folder directory enter: **python run.py**
2. From your browser visit: **http://127.0.0.1:3001/**

The web app will load with various visulazations, explore the web app tabs for more data and visualizations.

## Library Dependencies

* Pandas
* Numpy 
* PySpark
* Datetime
* Time
* Plotly
* Flask
* Json

## Results

I was able to make several conclusion based on my analysis: <br>

* Page interactions constitued most of my engineered variables and had the greatest covariance with customer churn
* The algorithm had an f1 score and accuracy of 72-75% based on the number of engineered features for the testing data
* This algorithm can scale to a distributed spark cluster to run a 12GB dataset through AWS which is the ultimate goal of this project

In conlcusion I made a model which would improve how Sparkify identifies users who will churn and can incentivize them to stay before they leave.

