# azure_flask_deployment
HHA 504 week 2 assignment

***

# Step-By-Step-Guide

## PART A: Setting Up Flask Application 

1. create an app.py file that will hold the main application code. Input the following code as a base: 

2. Create a folder names 'templates'
    </br>
    a. This folder will hold the html files that the app.py file links together 

3. In the folder, create html files labeled: about.html, base.html, data.html, and random.html
    </br>
    a. names and number of html files can be changed to fit preferences; make sure to change app.py code to accomodate for all the html files

4. create a requirements.txt file and import neceaasry pacakges: faker, pandas, flask

5. Create a dataset foler to inport dataset into

## PART B: Deploying on Azure App Service 

1. First Install Azure into IDE using this in terminal: 

>curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

2. then log into azure with: 

>az login --use-device-code

3. copy the code given and go the link proved. Log in with the code. 

4. Get az student subscription ID with: 

>az account list --output table

5. change subscription to azure for student ID: 

>az account set --subscription yoursubscriptionId

6. Go to azure and create a new resource group

7. For first time creating a webapp, use this in terminal: 

>az webapp up --resource-group <groupname> --name <app-name> --runtime <PYTHON:3.9> --sku <B1> 

8. After, to deploy new changes made to webpage to the cloud, use: 

>az webapp up

***

# Deployed URL 
joyce-504-flask.azurewebsites.net
