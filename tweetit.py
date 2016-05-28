
import tweepy

#NPG class deals with all housekeeping for creating instances.
class Tweet:
	def __init__(self):
		self.auth = tweepy.OAuthHandler(self.consumer_key,self.consumer_secret)
		self.auth.set_access_token(self.access_token, self.access_token_secret)
		self.handle = tweepy.API(self.auth)

	def get_handle(self):
		return self.handle

	def hitme(self,str):
		self.handle.update_status(str)
		print 'posted succesfully'

	def hit_with_image(self,fil,status=None):
		self.handle.update_with_media(fil,status=status)
		print 'Done successfully'

	def rehit(self,str):
		self.handle.retweet(str)
		print 'Done successfully'



class QUOTE(Tweet):
	#My Twitter consumer key
	
	consumer_key='DCpxbVNiAaXfn3rAmuuG0Cew7'
	
	#My consumer secret
	
	consumer_secret='oV9njr8Dax1JNNu2hbqE6AsBpv28teuxUHkMjHs5Kew0TM92sB'
	
	#My access token
	access_token='701008448360546304-bCi8zCIJJD2D5oMJj1DXf8n9Q7IVntw'
	
	#My access token secret
	access_token_secret='UUm10vwmLGgV8vrTPewUCl0HfmlkbjKpmSfrUiLFAVGy1'

