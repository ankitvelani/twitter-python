from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "164629846-7molrihvswyFG0eY7YQoanU8fNZxV51DLL39lMUK"
access_token_secret = "Qio7a95S1zgotg6AcirbumyyrHTAgezYn0o6FBex9hT77"
consumer_key = "jt8JvXvvhDm0VlrfSGuKFsnn9"
consumer_secret = "tzfFUZr5esq1zeStzDuzYf5u7kyoK41Jto9dEEtFRh9muCMv2T"
obj=open("rayen.txt","a")  
# Basic Listener that just prints recieved tweets to stdout
class StdOutListener(StreamListener):
    def on_data(self,data):
        obj.write(data)  
	 
        return True
    def on_error(self,status):
	obj.close()  
        print status

if __name__=='__main__':
    l=StdOutListener()
    auth=OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    stream=Stream(auth,l)
    
    #
    stream.filter(track=['RyanSchoolMurder','PradyumnWantsJustice','rayaninternationalschool'])
