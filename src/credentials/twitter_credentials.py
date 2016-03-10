import ConfigParser
import sys 
from credentials import Credentials
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy


class TwitterCredentials(Credentials):
	"""Defines a class which manages a set of twitter credentials. This class currently only supports the tweepy api.
	"""
	def __init__(self,credentialFileName=None,user_name=None,consumer_key=None,consumer_secret=None,access_token=None,access_token_secret=None):
		"""Defines a class which manages a set of twitter credentials. 
		Args:
			credentialFileName: The name of a file which contains the twitter credentials.
			user_name: The name of the user on twitter. 
			consumer_key: The consumer key of the api. 
			consumer_secret: The consumer secret of the api.
			access_token: The access_token of the api. 
			access_token_secret: The access_token_secret of the api.
		"""
		# If a credential fileName is passed in, 
		self._consumer_key = None
		self._consumer_secret = None 
		self._access_token = None 
		self._access_token_secret = None 
		self._user_name = None
		# Check to see if we passed in consumerkeys,consumer seacrets, etc. 

		# If a user_name was passed in, _user_name equal to it.
		if user_name is not None:
			self._user_name = user_name

		# If a consumer_key was passed in, set _consumer_key equal to it.
		if consumer_key is not None:
			self._consumer_key = consumer_key

		# If a consumer_secret was passed in, set _consumer_secret equal to it.
		if consumer_secret is not None:
			self._consumer_secret = consumer_secret

		# If an access_token was passed in, set _access_token equal to it.
		if access_token is not None:
			self._access_token = access_token

		# If an access_token_secret was passed in, set _access_token_secret equal to it.
		if access_token_secret is not None:
			self._access_token_secret = access_token_secret


		# If a credentialFileName was passed in, parse the values
		if credentialFileName != None:
			self.read_configuration_file(credentialFileName)


	def read_configuration_file(self,configurationFileName,config_type='ini'):
		"""Reads a configuration file. 
		Args:
			configurationFileName: The name of a configuration file. 
			config_type: The format of the configuration file. 
		"""
		result = None
		try:
			result = open(configurationFileName,'r')
		except IOError as e:
			print("I/O error({0}): {1}".format(e.errno,e.strerror))


		# If opening the configuration file was successful, parse it
		if result is not None:
			result.close()
			if config_type == 'ini':
				twitter_configuration = ConfigParser.ConfigParser()
				twitter_configuration.read(str(configurationFileName))
				
				# Check to see if the configuration file has a username 
				if twitter_configuration.has_option('TwitterAPI','user_name'):
					self._user_name=twitter_configuration.get('TwitterAPI','user_name')

				# Check to see if the configuration file has a consumer_key 
				if twitter_configuration.has_option('TwitterAPI','consumer_key'):
					self._consumer_key=twitter_configuration.get('TwitterAPI','consumer_key')
				
				# Check to see if the configuration file has a consumer_secret
				if twitter_configuration.has_option('TwitterAPI','consumer_secret'):
					self._consumer_secret=twitter_configuration.get('TwitterAPI','consumer_secret')

				# Check to see if the configuration file has an access_token
				if twitter_configuration.has_option('TwitterAPI','access_token'):
					self._access_token=twitter_configuration.get('TwitterAPI','access_token')

				# # Check to see if the configuration file has an access_token_secret
				if twitter_configuration.has_option('TwitterAPI','access_token_secret'):
					self._access_token_secret=twitter_configuration.get('TwitterAPI','access_token_secret')
			else:
				print("Error: {0} Not Supported".format(config_type))

	def create_authorization(self,api='tweepy'):
		"""Creates an authorization for the tweepy api. 
		Args:
			api: The specific api to use. Currently only supports tweepy
		Returns: An authorization for the tweepy api.
		"""
		if self._consumer_key is None or self._consumer_secret is None or self._access_token is None or self._access_token_secret is None:
			print("Error: Unable to create authorization: ")
			if self._consumer_key is None:
				print("\tconsumer_key does not exist.")
			if self._consumer_key is None:
				print("\tconsumer_secret does not exist.")
			if self._consumer_key is None:
				print("\taccess_token does not exist.")
			if self._consumer_key is None:
				print("\taccess_token_secret does not exist.")
			return None 
		else: 
			if api == 'tweepy':
				try:
					from tweepy import OAuthHandler 
				except ImportError as e:
					print("Error: failed to import module: {0}".format(e))
					return None 
				auth = tweepy.OAuthHandler(self._consumer_key,self._consumer_secret)
				auth.set_access_token(self._access_token,self._access_token_secret)
				return auth
			else:
				print("Error: Api Not supported.")
				return None


	def __str__(self):
		"""Creates a string with the twitter credental attributes. 
		Returns: A string with the TwitterAPI Attributes
		"""
		heading = 'TwitterAPI'
		userName = 'user_name: {0}'.format(self._user_name)

		consumerKey = 'consumer_key: {0}'.format(self._consumer_key)
		consumerSecret = 'consumer_secret: {0}'.format(self._consumer_secret)

		accessToken = 'access_token: {0}'.format(self._access_token)
		accessTokenSecret = 'access_token_secret: {0}'.format(self._access_token_secret)

		return '{0}\n{1}\n\t{2}\n\t{3}\n\t{4}\n\t{5}\n'.format(heading,userName,consumerKey,consumerSecret,accessToken,accessTokenSecret)

	def write_to_configuration_file(self,fileName=None,format='ini'):
		"""Writes TwitterAPI user information to a file if supplied one. 
		Args: 
			fileName: The name of the file to write to. 
			format: The format to present the api information.
		Returns: 
			None if format is not supported or information was written to file. 
			A string if no file was passed in. 
		"""
		if format == 'ini':
			heading = '[TwitterAPI]'
			userName = 'user_name={0}'.format(self._user_name)

			consumerKey = 'consumer_key={0}'.format(self._consumer_key)
			consumerSecret = 'consumer_secret: {0}'.format(self._consumer_secret)

			accessToken = 'access_token={0}'.format(self._access_token)
			accessTokenSecret = 'access_token_secret={0}'.format(self._access_token_secret)

			toPrint = '{0}\n{1}\n{2}\n{3}\n{4}\n{5}\n'.format(heading,userName,consumerKey,consumerSecret,accessToken,accessTokenSecret)
			
			# If a filename was passed in, write it to the file
			if fileName is not None:
				outputFile = open(fileName,'w')
				outputFile.write(toPrint)
				outputFile.close()
			else:
				return toPrint
		else:
			print("Error: {0} not supported".format(format))
			return None
				




		

