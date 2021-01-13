# Spark Supervised Learning for Customer Churn
## Project Motivation
The data I will be analyzing is from a fictious company called Sparkify. It works similarily to Spotify. It is a subscription based music service with two tiers of users, free and premium plan. Users can upgrade from free or downgrade from premium at any time and may aslo cancel their service all together.<br>

[Customer Churn](https://www.investopedia.com/terms/c/churnrate.asp) is a metric which measures the rate at which customers stop doing business with an entity. In our case when customers move from Sparkify's paid service level to free.<br>

Predicting churn rates is a challenging and common problem that data scientists and analysts regularly encounter in any customer-facing business. Additionally, the ability to efficiently manipulate large datasets with Spark is one of the highest-demand skills in the field of data.<br>

## Project Description
To make a scalable solution the project is broken down into three stages:<br>

>1. Exploratory Data Analysis
>2. Feature Engineering and Scaling
>3. Modelling

I made use of sparks declarative and imperative programming in steps 1 and 2. I explored all variables and found 4 neccessary to engineer the remaining necessary. I scaled them to appropriate dimensions. Then I modelled the data using several machine learning algorithms from which I chose one with the best metrics and performance so my solution could scale.

## File Description
The dataset for this project originates from IBM Watson. The data I investigate here consists of small changes to the original dataset, such as removing duplicates and mapping the email to a user id and removing the email column. 

>* **Sparkify.ipynb**: detailed analysis report <br>
>* **mini_event_data.json**: subset of data for use in Sparkify.ipynb for creating scalable solution for Spark cluster on AWS<br>
>* **app.py**: known solutions for comparison <br>
>* **run.py**: creates flask app to display webpage
>* **master.html**: main page of web app 
>* **go.html**: classification result page of web app

## Results

I was able to make several conclusion based on my analysis: <br>

* Page interactions constitued most of my engineered variables and had the greatest covariance with customer churn
* The algorithm had an f1 score and accuracy of 100% based on the number of engineered features for the testing data
* This algorithm can scale to a distributed spark clustere run on a 12GB dataset through AWS

In conlcusion I made a model which would improve how Sparkify identifies users who will churn and can incentivize them to stay before they leave.

