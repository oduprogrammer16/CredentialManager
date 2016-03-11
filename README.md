# CredentialManager
* Used for managing credentials for APIs
* This is a work in progress and has limited capabilities for managing credentials for various apis. 
* Currently designed to work with the tweepy api. 
* Stay Posted for updates as functionallity added. 

## About 

## Introduction
When I was taking Introduction to Web Science at Old Dominion University, I had to do several projects which required the use of the twitter api. A lot of my assignments could not have been completed successfully without the use of the tweepy library in python. 

One of the problems I encountered was finding ways to manage my twitter api access tokens. Initially, this was done through the use of a json file, which did not work as well as I had hoped. I then looked into other formats to storing my access tokens and discovered the config parser library in python. I decided to try out the config parser and poof, this project was born. 

## Goals 
The goal of this project is to allow a developer to store their credentials to various api's in a single file and to have quick simple access to their credentials when they need them. 

## Usage 
Usage of this project is relatively simple. 

1) Copy the folder credentials to wherever your project is located 
2) Edit your credentials in the sample .ini file provided 
3) Insert the following statements into your code wherever you need your credentials. 

 ```
 
 configFileName = 'blankTwitterCredentials.ini'
 credentialSet = credentials.twitter_credentials.TwitterCredentials(configFileName)
 
 # Simply prints your credentials 
 print(str(credentialSet))
 # Create an authorization with the twitter credentials.
 auth = credentialSet.create_authorization()
 
 ```
