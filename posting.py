# Python script to automate posting on Twitter and Facebook
from twython import Twython
import facebook
def post_to_twitter(api_key, api_secret, access_token, access_token_secret, message):
twitter = Twython(api_key, api_secret, access_token, access_token_secret)
twitter.update_status(status=message)
def post_to_facebook(api_key, api_secret, access_token, message):
graph = facebook.GraphAPI(access_token)
graph.put_object(parent_object='me', connection_name='feed', message=message)
