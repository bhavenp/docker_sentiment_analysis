# Deployable Sentiment Analysis model

This repo is for developing a sentiment analysis model that can be deployed on an AWS EKS cluster. 
1. There will be a single Docker container that will serve as an endpoint. Prediction will be served from this endpoint.
2. I want to add a container that controls a GUI.
3. I want to add a container that runs a SQL database that will store previous queries to the model and the results.

