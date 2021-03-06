# CredentialManager

## Requirements 
* Python 2.7 

## About 

### Introduction
When I was taking Introduction to Web Science at Old Dominion University, I had to do several projects which required the use of the twitter api. A lot of my assignments could not have been completed successfully without the use of the tweepy library in python. 

One of the problems I encountered was finding ways to manage my twitter api access tokens. Initially, this was done through the use of a json file, which did not work as well as I had hoped. I then looked into other formats to storing my access tokens and discovered the config parser library in python. I decided to try out the config parser and found it to be simple and effective which lead to this project's creation. 

### Goals 
The goal of this project is to allow a developer to store their credentials to various api's in a single file and to have quick simple access to their credentials when they need them. 

## Usage 
Usage of this project is relatively simple. 

1) Copy the folder credentials to wherever your project is located. 
 * **Note** Due to a small problem with the library, your project must be set as seen below. 
 ```
 
Your_Project
|
|
+----credentials
|    |
|    | __init__.py
|    | credentials.py
|    | twitter_credentials.py
|
+----Your source code files 
|    | 
|    | Your_credentials_file.ini
|    | your_main_project_code_using_credentials.py 
```

2) Edit your credentials in the sample .ini file provided or in a .ini file in using the format below: 

```
[TwitterAPI]
user_name=Undefined
consumer_key=Undefined 
consumer_secret=Undefined
access_token=Undefined
access_token_secret=Undefined

```

3) Insert the following statements into your code wherever you need your credentials. 
 
 ```python
 


from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
import sys 

sys.path.insert(0,'../credentials')
import twitter_credentials

if __name__=='__main__':
	configFileName = 'blankTwitterCredentials.ini'
	credentialSet = twitter_credentials.TwitterCredentials(configFileName)
	
	print(str(credentialSet))

	# Create an authorization with the twitter credentials.
	auth = tweepy.OAuthHandler(credentialSet.consumer_key,credentialSet.consumer_secret)
	auth.set_access_token(credentialSet.access_token,credentialSet.access_token_secret)
	
	api = tweepy.API(auth)
	try:
		api.verify_credentials()
		print("Successfully logged in.")
	except: 
		pass
 
 ```

## Additional Notes
   
* A setup.py file is under development and eventually aid installation of this project. 
* Additional features are planned and will be designed to expand usage of this project.  

## Revision History 

### 4/9/15

* Originally this project was planned to be designed to work with the tweepy api. After careful consideration, this project will not perform functions for the tweepy api and will soley be used to manage credential set. 

