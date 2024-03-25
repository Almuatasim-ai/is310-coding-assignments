import json
from TikTokApi import TikTokApi

class Hashtag:
    def __init__(self, api):
        self.api = api
    def get_videos_by_hashtag(self, name):
        return self.api.by_hashtag(hashtag=name, count=100)  # Get 100 videos that used the specified hashtag
    
    async def print_videos(self, name):
        hashtag = self.api.hashtag(name=name)
        async for video in hashtag.videos():
            print(video.id)
    def extract_hashtags(self, response):
        data = json.loads(response)
        hashtags = []
        for item in data['data']:
            words = item['description'].split()
            hashtags.extend(word for word in words if word.startswith('#'))
        return hashtags

# Usage
api = TikTokApi.get_instance(custom_verifyFp="your_custom_verifyFp_value_here")
hashtag_obj = Hashtag(api)
videos = hashtag_obj.get_videos_by_hashtag('freepalestine')

for video in videos:
    print(video['desc'])