from pprint import pprint
from pyyoutube import Api
import requests
import textdistance
import cleantext
# api = Api(api_key="AIzaSyDnw3XP9UVJ_DXYQjBwNN6HHR1Bzl2LpkM")

# channel_by_id = api.get_channel_info(channel_id="UCXDKyqRyXEDQAEIUi5nYFNg")
# print(channel_by_id.items[0].to_dict())

# data = requests.get('https://www.googleapis.com/youtube/v3/search?key=AIzaSyDnw3XP9UVJ_DXYQjBwNN6HHR1Bzl2LpkM&channelId=UCXDKyqRyXEDQAEIUi5nYFNg&part=snippet,id&order=date&maxResults=20')

# print(data.json())



# data = requests.get('https://www.googleapis.com/youtube/v3/search?key=AIzaSyDnw3XP9UVJ_DXYQjBwNN6HHR1Bzl2LpkM&channelId=UCXDKyqRyXEDQAEIUi5nYFNg&part=snippet,id&order=date&maxResults=20')

# print(data.json())

def videoscore(video_id):

    res = requests.get('https://www.googleapis.com/youtube/v3/videos?key=AIzaSyDnw3XP9UVJ_DXYQjBwNN6HHR1Bzl2LpkM&fields=items(snippet(title,description,tags))&part=snippet&id='+str(video_id))


    data = res.json()
    #pprint(data)
    try:
        # if data['items'][0]['snippet']['tags']:
        #     print(data['items'][0]['snippet']['tags'])
        
        title = cleantext.clean_words(str(data['items'][0]['snippet']['title']))
        description = cleantext.clean_words(str(data['items'][0]['snippet']['description']))
        tags = data['items'][0]['snippet']['tags']

        #print(title)

        score=0

        for word in title:
            for tag in tags:
                point = textdistance.hamming(word, tag)
                if point <= 4:
                    if score < 10:
                        score = score + 4
                    #print("Score for { "+word+" } from title and { "+tag+" } from tags = "+str(score) )

        for word in description:
            for tag in tags:
                point = textdistance.hamming(word, tag)
                if point <= 4:
                    if score < 10:
                        score = score + 4
        
        return score
    # # print(score)
    # # if score > 20:
    # #     print('Congradulations , Your Video is well optimized')
    # # else:
    # #     print('Needs to be optimized'

    except Exception as e:
        print("Tags not Found") 
        return 0
    # # data = {
    # #     "items":[
    # #     {
    # #         "snippet":{
    # #             "title":"Passwordless Authentication with NextJS and Stytch",
    # #             "description":"Check out stytch here: https://stytch.com/?utm_source=youtube&utm_medium=paid_sponsor&utm_campaign=scalablescripts-april&utm_content=magic-link-1\n\nStytch is building the developer platform for passwordless authentication. They make it easy for you to embed passwordless solutions into your websites and apps for better security, better conversion rates, and a better end-user experience.\n\n#nextjs #stytch #passwordless",
    # #             "tags":[
    # #                 "coding",
    # #                 "programming",
    # #                 "full stack development",
    # #                 "scalable scripts",
    # #                 "programming tutorials",
    # #                 "developer",
    # #                 "coder",
    # #                 "software",
    # #                 "laravel",
    # #                 "react",
    # #                 "vue",
    # #                 "angular",
    # #                 "django",
    # #                 "python",
    # #                 "nestjs",
    # #                 "nextjs",
    # #                 "nuxtjs",
    # #                 "golang",
    # #                 "denojs",
    # #                 "nodejs",
    # #                 "microservices",
    # #                 "docker",
    # #                 "kubernetes",
    # #                 "rabbitmq",
    # #                 "kafka",
    # #                 "event driven architecture",
    # #                 "event driven design",
    # #                 "containers",
    # #                 "mircorservices architecture",
    # #                 "api",
    # #                 "spa",
    # #                 "single page application",
    # #                 "c#",
    # #                 "java",
    # #                 "kotlin",
    # #                 ".net core",
    # #                 "java spring boot"
    # #             ]
    # #         }
    # #     }
    # #     ]
    # # }

    # #title  = str(data['items'][0]['snippet']['title']).split(' ')
    




