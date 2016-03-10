

import credentials.twitter_credentials 


if __name__=='__main__':
	configFileName = 'blankTwitterCredentials.ini'
	credentialSet = credentials.twitter_credentials.TwitterCredentials(configFileName)
	print(str(credentialSet))