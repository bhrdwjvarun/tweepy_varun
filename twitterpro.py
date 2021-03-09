import tweepy


#copy paste your access tokens here

auth = tweepy.OAuthHandler('', '')
auth.set_access_token('', '')

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text.encode('utf-8'))

user = api.get_user('#username')
print('username = ' , user.screen_name)
print('followers = ' , user.followers_count)
print('These are the friends of',user.screen_name,'on twitter')
for friend in user.friends():
   print(friend.screen_name)