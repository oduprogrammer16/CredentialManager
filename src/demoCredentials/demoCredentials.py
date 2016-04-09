

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
	auth = credentialSet.create_authorization()
	api = tweepy.API(auth)
	try:
		api.verify_credentials()
		print("Successfully logged in.")
	except: 
		pass

