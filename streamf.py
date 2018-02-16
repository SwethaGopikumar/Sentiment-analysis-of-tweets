
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time


access_token = ""
access_token_secret = ""
consumer_key = ''
consumer_secret = ""
tweet=[]

class StdOutListener(StreamListener):

    def on_data(self, data):
        try:

            savedata=open('indvsnz.csv','a')
            savedata.write(data)
            savedata.write('\n')
            savedata.close()
            
        
            return True

        except Exception as e:
           print ('failed ondata,',str(e))
           time.sleep(5)
    def on_error(self,status)       :
        print(status)


if __name__ == '__main__':

    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    stream.filter(languages=["en"],track=['INDvNZ','indvnz','team india','blackcaps','TeamIndia','IndvNZ']) 
 
