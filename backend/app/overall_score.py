import requests
from .video_score import videoscore
from pprint import pprint
# total = S1 + S2 + S3 + S4 + S5;
# average = total/5.0;
# percentage = (total / 500.0) * 100;

# #Print the result
# print(“Total marks = “, total)
# print(“Average marks = “, average)
# print(“Percentage = “, percentage)

def overall_score(channel_id):
    data = requests.get('https://www.googleapis.com/youtube/v3/search?key=AIzaSyDnw3XP9UVJ_DXYQjBwNN6HHR1Bzl2LpkM&channelId='+str(channel_id)+'&part=snippet,id&order=date&maxResults=20')
    #print(data.json())
    # json_data = [
    #         {
    #             "kind": "youtube#searchResult",
    #             "etag": "o40hm9DSjOab8Zr4bneoYQbhsfM",
    #             "id": {
    #                 "kind": "youtube#video",
    #                 "videoId": "wzeomGUdlnI"
    #             },
    #             "snippet": {
    #                 "publishedAt": "2022-11-18T00:07:53Z",
    #                 "channelId": "UCXDKyqRyXEDQAEIUi5nYFNg",
    #                 "title": "Django and Celery with Docker Running Periodic Task. Building automated web scraper.",
    #                 "description": "in this video we are going to learn how to run periodic task with celery in django. we will be building an automated web scraper.",
    #                 "thumbnails": {
    #                     "default": {
    #                         "url": "https://i.ytimg.com/vi/wzeomGUdlnI/default.jpg",
    #                         "width": 120,
    #                         "height": 90
    #                     },
    #                     "medium": {
    #                         "url": "https://i.ytimg.com/vi/wzeomGUdlnI/mqdefault.jpg",
    #                         "width": 320,
    #                         "height": 180
    #                     },
    #                     "high": {
    #                         "url": "https://i.ytimg.com/vi/wzeomGUdlnI/hqdefault.jpg",
    #                         "width": 480,
    #                         "height": 360
    #                     }
    #                 },
    #                 "channelTitle": "Henry Coding stack",
    #                 "liveBroadcastContent": "none",
    #                 "publishTime": "2022-11-18T00:07:53Z"
    #             }
    #         },
    #         {
    #             "kind": "youtube#searchResult",
    #             "etag": "lErRWDjYC6boSUDaUdKz9IpbGrQ",
    #             "id": {
    #                 "kind": "youtube#video",
    #                 "videoId": "Y2WwBJVePro"
    #             },
    #             "snippet": {
    #                 "publishedAt": "2022-11-13T02:32:04Z",
    #                 "channelId": "UCXDKyqRyXEDQAEIUi5nYFNg",
    #                 "title": "Django and Celery tutorial.  Running Background Task",
    #                 "description": "in this video you are going to learn how to processing task to run at the background. learn how to improve your application ...",
    #                 "thumbnails": {
    #                     "default": {
    #                         "url": "https://i.ytimg.com/vi/Y2WwBJVePro/default.jpg",
    #                         "width": 120,
    #                         "height": 90
    #                     },
    #                     "medium": {
    #                         "url": "https://i.ytimg.com/vi/Y2WwBJVePro/mqdefault.jpg",
    #                         "width": 320,
    #                         "height": 180
    #                     },
    #                     "high": {
    #                         "url": "https://i.ytimg.com/vi/Y2WwBJVePro/hqdefault.jpg",
    #                         "width": 480,
    #                         "height": 360
    #                     }
    #                 },
    #                 "channelTitle": "Henry Coding stack",
    #                 "liveBroadcastContent": "none",
    #                 "publishTime": "2022-11-13T02:32:04Z"
    #             }
    #         },
    #         {
    #             "kind": "youtube#searchResult",
    #             "etag": "JC4VFwUmltqUlsnh6nGbv1r8lbY",
    #             "id": {
    #                 "kind": "youtube#video",
    #                 "videoId": "_HzBC1b2bao"
    #             },
    #             "snippet": {
    #                 "publishedAt": "2022-11-13T01:49:09Z",
    #                 "channelId": "UCXDKyqRyXEDQAEIUi5nYFNg",
    #                 "title": "Django And Celery tutorial with docker for beginners",
    #                 "description": "Welcome to the Django and Celery Series. This tutorial stream is dedicated to exploring the use of celery within Django. if you are ...",
    #                 "thumbnails": {
    #                     "default": {
    #                         "url": "https://i.ytimg.com/vi/_HzBC1b2bao/default.jpg",
    #                         "width": 120,
    #                         "height": 90
    #                     },
    #                     "medium": {
    #                         "url": "https://i.ytimg.com/vi/_HzBC1b2bao/mqdefault.jpg",
    #                         "width": 320,
    #                         "height": 180
    #                     },
    #                     "high": {
    #                         "url": "https://i.ytimg.com/vi/_HzBC1b2bao/hqdefault.jpg",
    #                         "width": 480,
    #                         "height": 360
    #                     }
    #                 },
    #                 "channelTitle": "Henry Coding stack",
    #                 "liveBroadcastContent": "none",
    #                 "publishTime": "2022-11-13T01:49:09Z"
    #             }
    #         },
    #         {
    #             "kind": "youtube#searchResult",
    #             "etag": "XZ8HsZymZajkd-7JMXkfmSTIWVU",
    #             "id": {
    #                 "kind": "youtube#video",
    #                 "videoId": "WuluKqRu6xY"
    #             },
    #             "snippet": {
    #                 "publishedAt": "2022-11-12T03:35:59Z",
    #                 "channelId": "UCXDKyqRyXEDQAEIUi5nYFNg",
    #                 "title": "Dockerizing your Django project for beginners",
    #                 "description": "In this video, you'll learn how to Dockerize your Django project . Docker is a great tool that I've used in almost all of my projects.",
    #                 "thumbnails": {
    #                     "default": {
    #                         "url": "https://i.ytimg.com/vi/WuluKqRu6xY/default.jpg",
    #                         "width": 120,
    #                         "height": 90
    #                     },
    #                     "medium": {
    #                         "url": "https://i.ytimg.com/vi/WuluKqRu6xY/mqdefault.jpg",
    #                         "width": 320,
    #                         "height": 180
    #                     },
    #                     "high": {
    #                         "url": "https://i.ytimg.com/vi/WuluKqRu6xY/hqdefault.jpg",
    #                         "width": 480,
    #                         "height": 360
    #                     }
    #                 },
    #                 "channelTitle": "Henry Coding stack",
    #                 "liveBroadcastContent": "none",
    #                 "publishTime": "2022-11-12T03:35:59Z"
    #             }
    #         },
    #         {
    #             "kind": "youtube#searchResult",
    #             "etag": "go1GKphzllW9Cr7g-rkYBaiLu4c",
    #             "id": {
    #                 "kind": "youtube#video",
    #                 "videoId": "PyJczJwZNeU"
    #             },
    #             "snippet": {
    #                 "publishedAt": "2022-07-17T14:02:25Z",
    #                 "channelId": "UCXDKyqRyXEDQAEIUi5nYFNg",
    #                 "title":"Stripe payment with django rest framework and reactjs part 2 .   custom payment workflow","description":"hello django developer welcome to another django rest framework and reactjs with stripe tutorial. in this tutorial we are going to ...","thumbnails": {
    #                     "default": {
    #                         "url": "https://i.ytimg.com/vi/PyJczJwZNeU/default.jpg",
    #                         "width": 120,
    #                         "height": 90
    #                     },
    #                     "medium": {
    #                         "url": "https://i.ytimg.com/vi/PyJczJwZNeU/mqdefault.jpg",
    #                         "width": 320,
    #                         "height": 180
    #                     },
    #                     "high": {
    #                         "url": "https://i.ytimg.com/vi/PyJczJwZNeU/hqdefault.jpg",
    #                         "width": 480,
    #                         "height": 360
    #                     }
    #                 },
    #                 "channelTitle": "Henry Coding stack",
    #                 "liveBroadcastContent": "none",
    #                 "publishTime": "2022-07-17T14:02:25Z"
    #             }
    #         },
    #         {
    #             "kind": "youtube#searchResult",
    #             "etag": "xX88pzwExfLAb0KMK0uRrR5E_Dg",
    #             "id": {
    #                 "kind": "youtube#video",
    #                 "videoId": "rKD5bhoTeFw"
    #             },
    #             "snippet": {
    #                 "publishedAt": "2022-07-03T01:59:07Z",
    #                 "channelId": "UCXDKyqRyXEDQAEIUi5nYFNg",
    #                 "title": "Stripe Payment with Django REST framework and reactjs Tutorial",
    #                 "description": "hello django developer its been a while, glad to be back. in today tutorial we are going to learn how to integrate stripe payment in ...",
    #                 "thumbnails": {
    #                     "default": {
    #                         "url": "https://i.ytimg.com/vi/rKD5bhoTeFw/default.jpg",
    #                         "width": 120,
    #                         "height": 90
    #                     },
    #                     "medium": {
    #                         "url": "https://i.ytimg.com/vi/rKD5bhoTeFw/mqdefault.jpg",
    #                         "width": 320,
    #                         "height": 180
    #                     },
    #                     "high": {
    #                         "url": "https://i.ytimg.com/vi/rKD5bhoTeFw/hqdefault.jpg",
    #                         "width": 480,
    #                         "height": 360
    #                     }
    #                 },
    #                 "channelTitle": "Henry Coding stack",
    #                 "liveBroadcastContent": "none",
    #                 "publishTime": "2022-07-03T01:59:07Z"
    #             }
    #         },
    #         {
    #             "kind": "youtube#searchResult",
    #             "etag": "n4ki9j9um-W_crfXLcLWaAPqqSc",
    #             "id": {
    #                 "kind": "youtube#video",
    #                 "videoId": "UnAhR6SlM90"
    #             },
    #             "snippet": {
    #                 "publishedAt": "2022-02-20T23:29:02Z",
    #                 "channelId": "UCXDKyqRyXEDQAEIUi5nYFNg",
    #                 "title": "Django Rest framework Tutorial. Multiple user authentication in Rest API. part 2",
    #                 "description": "hello django developer, in this tutorial we are going to learn how to implement multiple users with different role in a rest api ...",
    #                 "thumbnails": {
    #                     "default": {
    #                         "url": "https://i.ytimg.com/vi/UnAhR6SlM90/default.jpg",
    #                         "width": 120,
    #                         "height": 90
    #                     },
    #                     "medium": {
    #                         "url": "https://i.ytimg.com/vi/UnAhR6SlM90/mqdefault.jpg",
    #                         "width": 320,
    #                         "height": 180
    #                     },
    #                     "high": {
    #                         "url": "https://i.ytimg.com/vi/UnAhR6SlM90/hqdefault.jpg",
    #                         "width": 480,
    #                         "height": 360
    #                     }
    #                 },
    #                 "channelTitle": "Henry Coding stack",
    #                 "liveBroadcastContent": "none",
    #                 "publishTime": "2022-02-20T23:29:02Z"
    #             }
    #         },
    #         {
    #             "kind": "youtube#searchResult",
    #             "etag": "m1lLJJ2YJLvNpWV5aqaTvldMmfo",
    #             "id": {
    #                 "kind": "youtube#video",
    #                 "videoId": "7TQufn2wCLc"
    #             },
    #             "snippet": {
    #                 "publishedAt": "2022-01-28T22:31:58Z",
    #                 "channelId": "UCXDKyqRyXEDQAEIUi5nYFNg",
    #                 "title": "Django Rest framework Tutorial. Multiple user authentication in Rest API. part 1",
    #                 "description":"hello django developer, today we are going to learn how to implement multiple users with different role in a rest api environment ...","thumbnails": {
    #                     "default": {
    #                         "url": "https://i.ytimg.com/vi/7TQufn2wCLc/default.jpg",
    #                         "width": 120,
    #                         "height": 90
    #                     },
    #                     "medium": {
    #                         "url": "https://i.ytimg.com/vi/7TQufn2wCLc/mqdefault.jpg",
    #                         "width": 320,
    #                         "height": 180
    #                     },
    #                     "high": {
    #                         "url": "https://i.ytimg.com/vi/7TQufn2wCLc/hqdefault.jpg",
    #                         "width": 480,
    #                         "height": 360
    #                     }
    #                 },
    #                 "channelTitle": "Henry Coding stack",
    #                 "liveBroadcastContent": "none",
    #                 "publishTime": "2022-01-28T22:31:58Z"
    #             }
    #         },
    #         {
    #             "kind": "youtube#searchResult",
    #             "etag": "Lw7e2KH9hV5fdviPxXvZWZtSzAE",
    #             "id": {
    #                 "kind": "youtube#video",
    #                 "videoId": "SyQGW8rvXaI"
    #             },
    #             "snippet": {
    #                 "publishedAt": "2022-01-05T16:01:33Z",
    #                 "channelId": "UCXDKyqRyXEDQAEIUi5nYFNg",
    #                 "title": "Django + Graphql and Reactjs Tutorial part 4 (authentication)",
    #                 "description": "hi django developer welcome to a new series where we will be exploring the power of graphql in our django project to build more ...",
    #                 "thumbnails": {
    #                     "default": {
    #                         "url": "https://i.ytimg.com/vi/SyQGW8rvXaI/default.jpg",
    #                         "width": 120,
    #                         "height": 90
    #                     },
    #                     "medium": {
    #                         "url": "https://i.ytimg.com/vi/SyQGW8rvXaI/mqdefault.jpg",
    #                         "width": 320,
    #                         "height": 180
    #                     },
    #                     "high": {
    #                         "url": "https://i.ytimg.com/vi/SyQGW8rvXaI/hqdefault.jpg",
    #                         "width": 480,
    #                         "height": 360
    #                     }
    #                 },
    #                 "channelTitle": "Henry Coding stack",
    #                 "liveBroadcastContent": "none",
    #                 "publishTime": "2022-01-05T16:01:33Z"
    #             }
    #         },
    #         {
    #             "kind": "youtube#searchResult",
    #             "etag": "dldKpIsXxvL82N12PUTafxzv2BI",
    #             "id": {
    #                 "kind": "youtube#video",
    #                 "videoId": "wTDeF5gPnek"
    #             },
    #             "snippet": {
    #                 "publishedAt": "2021-12-26T09:17:01Z",
    #                 "channelId": "UCXDKyqRyXEDQAEIUi5nYFNg",
    #                 "title": "Django + Graphql and Reactjs Tutorial",
    #                 "description": "hi django developer welcome to a new series where we will be exploring the power of graphql in our django project to build more ...",
    #                 "thumbnails": {
    #                     "default": {
    #                         "url": "https://i.ytimg.com/vi/wTDeF5gPnek/default.jpg",
    #                         "width": 120,
    #                         "height": 90
    #                     },
    #                     "medium": {
    #                         "url": "https://i.ytimg.com/vi/wTDeF5gPnek/mqdefault.jpg",
    #                         "width": 320,
    #                         "height": 180
    #                     },
    #                     "high": {
    #                         "url": "https://i.ytimg.com/vi/wTDeF5gPnek/hqdefault.jpg",
    #                         "width": 480,
    #                         "height": 360
    #                     }
    #                 },
    #                 "channelTitle": "Henry Coding stack",
    #                 "liveBroadcastContent": "none",
    #                 "publishTime": "2021-12-26T09:17:01Z"
    #             }
    #         },
    #         {
    #             "kind": "youtube#searchResult",
    #             "etag": "F8UB1b5TcExi4uZGP4fN2wGGADA",
    #             "id": {
    #                 "kind": "youtube#video",
    #                 "videoId": "MByCCf7l72E"
    #             },
    #             "snippet": {
    #                 "publishedAt": "2021-12-23T07:03:11Z",
    #                 "channelId": "UCXDKyqRyXEDQAEIUi5nYFNg",
    #                 "title": "Django + Graphql and Reactjs Tutorial",
    #                 "description": "hi django developer welcome to a new series where we will be exploring the power of graphql in our django project to build more ...",
    #                 "thumbnails": {
    #                     "default": {
    #                         "url": "https://i.ytimg.com/vi/MByCCf7l72E/default.jpg",
    #                         "width": 120,
    #                         "height": 90
    #                     },
    #                     "medium": {
    #                         "url": "https://i.ytimg.com/vi/MByCCf7l72E/mqdefault.jpg",
    #                         "width": 320,
    #                         "height": 180
    #                     },
    #                     "high": {
    #                         "url": "https://i.ytimg.com/vi/MByCCf7l72E/hqdefault.jpg",
    #                         "width": 480,
    #                         "height": 360
    #                     }
    #                 },
    #                 "channelTitle": "Henry Coding stack",
    #                 "liveBroadcastContent": "none",
    #                 "publishTime": "2021-12-23T07:03:11Z"
    #             }
    #         },
    #         {
    #             "kind": "youtube#searchResult",
    #             "etag": "s-KpCL7pg4Q0cTmCOqgY_VubZbE",
    #             "id": {
    #                 "kind": "youtube#video",
    #                 "videoId": "Ls7Y0PNFK7o"
    #             },
    #             "snippet": {
    #                 "publishedAt": "2021-12-23T05:55:59Z",
    #                 "channelId": "UCXDKyqRyXEDQAEIUi5nYFNg",
    #                 "title": "Building a backend REST API with Django REST framework  part8",
    #                 "description": "hi django developers, this is a Django rest framework For Beginners, in this video you will learn what an Api is , how to consume ...",
    #                 "thumbnails": {
    #                     "default": {
    #                         "url": "https://i.ytimg.com/vi/Ls7Y0PNFK7o/default.jpg",
    #                         "width": 120,
    #                         "height": 90
    #                     },
    #                     "medium": {
    #                         "url": "https://i.ytimg.com/vi/Ls7Y0PNFK7o/mqdefault.jpg",
    #                         "width": 320,
    #                         "height": 180
    #                     },
    #                     "high": {
    #                         "url": "https://i.ytimg.com/vi/Ls7Y0PNFK7o/hqdefault.jpg",
    #                         "width": 480,
    #                         "height": 360
    #                     }
    #                 },
    #                 "channelTitle": "Henry Coding stack",
    #                 "liveBroadcastContent": "none",
    #                 "publishTime": "2021-12-23T05:55:59Z"
    #             }
    #         },
    #         {
    #             "kind": "youtube#searchResult",
    #             "etag": "qkx9kQ15o2aaQLfhqCVe_ZcLp3A",
    #             "id": {
    #                 "kind": "youtube#video",
    #                 "videoId": "EU3DwWf12t4"
    #             },
    #             "snippet": {
    #                 "publishedAt": "2021-12-23T05:51:26Z",
    #                 "channelId": "UCXDKyqRyXEDQAEIUi5nYFNg",
    #                 "title": "Django  +  Graphql  &amp; Reactjs  tutorial",
    #                 "description": "hi django developer welcome to a new series where we will be exploring the power of graphql in our django project to build more ...",
    #                 "thumbnails": {
    #                     "default": {
    #                         "url": "https://i.ytimg.com/vi/EU3DwWf12t4/default.jpg",
    #                         "width": 120,
    #                         "height": 90
    #                     },
    #                     "medium": {
    #                         "url": "https://i.ytimg.com/vi/EU3DwWf12t4/mqdefault.jpg",
    #                         "width": 320,
    #                         "height": 180
    #                     },
    #                     "high": {
    #                         "url": "https://i.ytimg.com/vi/EU3DwWf12t4/hqdefault.jpg",
    #                         "width": 480,
    #                         "height": 360
    #                     }
    #                 },
    #                 "channelTitle": "Henry Coding stack",
    #                 "liveBroadcastContent": "none",
    #                 "publishTime": "2021-12-23T05:51:26Z"
    #             }
    #         },
    #         {
    #             "kind": "youtube#searchResult",
    #             "etag": "HgdmbHxI_QAGyuIEBBpVIYXUg2M",
    #             "id": {
    #                 "kind": "youtube#video",
    #                 "videoId": "r-JXSgx36mQ"
    #             },
    #             "snippet": {
    #                 "publishedAt": "2021-10-02T06:14:11Z",
    #                 "channelId": "UCXDKyqRyXEDQAEIUi5nYFNg",
    #                 "title": "Building a backend REST API with Django REST framework  part7( API Documentation)",
    #                 "description": "hi django developers, this is a Django rest framework For Beginners, in this video you will learn what an Api is , how to consume ...",
    #                 "thumbnails": {
    #                     "default": {
    #                         "url": "https://i.ytimg.com/vi/r-JXSgx36mQ/default.jpg",
    #                         "width": 120,
    #                         "height": 90
    #                     },
    #                     "medium": {
    #                         "url": "https://i.ytimg.com/vi/r-JXSgx36mQ/mqdefault.jpg",
    #                         "width": 320,
    #                         "height": 180
    #                     },
    #                     "high": {
    #                         "url": "https://i.ytimg.com/vi/r-JXSgx36mQ/hqdefault.jpg",
    #                         "width": 480,
    #                         "height": 360
    #                     }
    #                 },
    #                 "channelTitle": "Henry Coding stack",
    #                 "liveBroadcastContent": "none",
    #                 "publishTime": "2021-10-02T06:14:11Z"
    #             }
    #         },
    #         {
    #             "kind": "youtube#searchResult",
    #             "etag": "irW1xodV1I-3bJXPJRoUIVGp3Rs",
    #             "id": {
    #                 "kind": "youtube#video",
    #                 "videoId": "glsFQSAaRVQ"
    #             },
    #             "snippet": {
    #                 "publishedAt": "2021-08-28T21:15:14Z",
    #                 "channelId": "UCXDKyqRyXEDQAEIUi5nYFNg",
    #                 "title": "Build a Backend Rest API with Django REST framework  tutorial part 6",
    #                 "description":"hi django developers, this is a Django rest framework For Beginners, in this video you will learn what an Api is ,  how to come ...","thumbnails": {
    #                     "default": {
    #                         "url": "https://i.ytimg.com/vi/glsFQSAaRVQ/default.jpg",
    #                         "width": 120,
    #                         "height": 90
    #                     },
    #                     "medium": {
    #                         "url": "https://i.ytimg.com/vi/glsFQSAaRVQ/mqdefault.jpg",
    #                         "width": 320,
    #                         "height": 180
    #                     },
    #                     "high": {
    #                         "url": "https://i.ytimg.com/vi/glsFQSAaRVQ/hqdefault.jpg",
    #                         "width": 480,
    #                         "height": 360
    #                     }
    #                 },
    #                 "channelTitle": "Henry Coding stack",
    #                 "liveBroadcastContent": "none",
    #                 "publishTime": "2021-08-28T21:15:14Z"
    #             }
    #         },
    #         {
    #             "kind": "youtube#searchResult",
    #             "etag": "VEEyfraIjxmK63nLx3Lnf1YdR2o",
    #             "id": {
    #                 "kind": "youtube#video",
    #                 "videoId": "HISLmY4Bkuk"
    #             },
    #             "snippet": {
    #                 "publishedAt": "2021-08-17T08:00:03Z",
    #                 "channelId": "UCXDKyqRyXEDQAEIUi5nYFNg",
    #                 "title": "Build a Backend Rest API with Django REST framework tutorial part 5.    REST API Unit Testing",
    #                 "description": "hi django developers, this is a Django rest framework For Beginners, in this video you will learn what an Api is , how to consume ...",
    #                 "thumbnails": {
    #                     "default": {
    #                         "url": "https://i.ytimg.com/vi/HISLmY4Bkuk/default.jpg",
    #                         "width": 120,
    #                         "height": 90
    #                     },
    #                     "medium": {
    #                         "url": "https://i.ytimg.com/vi/HISLmY4Bkuk/mqdefault.jpg",
    #                         "width": 320,
    #                         "height": 180
    #                     },
    #                     "high": {
    #                         "url": "https://i.ytimg.com/vi/HISLmY4Bkuk/hqdefault.jpg",
    #                         "width": 480,
    #                         "height": 360
    #                     }
    #                 },
    #                 "channelTitle": "Henry Coding stack",
    #                 "liveBroadcastContent": "none",
    #                 "publishTime": "2021-08-17T08:00:03Z"
    #             }
    #         },
    #         {
    #             "kind": "youtube#searchResult",
    #             "etag": "I5vGP5N1fhyA403_Ow-rD6DZk9w",
    #             "id": {
    #                 "kind": "youtube#video",
    #                 "videoId": "M83EcD0j3t0"
    #             },
    #             "snippet": {
    #                 "publishedAt": "2021-08-13T21:00:42Z",
    #                 "channelId": "UCXDKyqRyXEDQAEIUi5nYFNg",
    #                 "title": "Build a Backend Rest API with Django REST framework  tutorial part 4",
    #                 "description": "hi django developers, this is a Django rest framework For Beginners, in this video you will learn what an Api is , how to consume ...",
    #                 "thumbnails": {
    #                     "default": {
    #                         "url": "https://i.ytimg.com/vi/M83EcD0j3t0/default.jpg",
    #                         "width": 120,
    #                         "height": 90
    #                     },
    #                     "medium": {
    #                         "url": "https://i.ytimg.com/vi/M83EcD0j3t0/mqdefault.jpg",
    #                         "width": 320,
    #                         "height": 180
    #                     },
    #                     "high": {
    #                         "url": "https://i.ytimg.com/vi/M83EcD0j3t0/hqdefault.jpg",
    #                         "width": 480,
    #                         "height": 360
    #                     }
    #                 },
    #                 "channelTitle": "Henry Coding stack",
    #                 "liveBroadcastContent": "none",
    #                 "publishTime": "2021-08-13T21:00:42Z"
    #             }
    #         },
    #         {
    #             "kind": "youtube#searchResult",
    #             "etag": "A565FM2_QxuaXlNx6nEodrwDxFE",
    #             "id": {
    #                 "kind": "youtube#video",
    #                 "videoId": "4U9E9xn5HaI"
    #             },
    #             "snippet": {
    #                 "publishedAt": "2021-08-13T19:20:41Z",
    #                 "channelId": "UCXDKyqRyXEDQAEIUi5nYFNg",
    #                 "title": "Build a Backend Rest API with Django REST framework Tutorial part 3",
    #                 "description":"hi django lovers, this is a Django rest framework For Beginners, in this video you will learn what an Api is , how to consume an Api ...","thumbnails": {
    #                     "default": {
    #                         "url": "https://i.ytimg.com/vi/4U9E9xn5HaI/default.jpg",
    #                         "width": 120,
    #                         "height": 90
    #                     },
    #                     "medium": {
    #                         "url": "https://i.ytimg.com/vi/4U9E9xn5HaI/mqdefault.jpg",
    #                         "width": 320,
    #                         "height": 180
    #                     },
    #                     "high": {
    #                         "url": "https://i.ytimg.com/vi/4U9E9xn5HaI/hqdefault.jpg",
    #                         "width": 480,
    #                         "height": 360
    #                     }
    #                 },
    #                 "channelTitle": "Henry Coding stack",
    #                 "liveBroadcastContent": "none",
    #                 "publishTime": "2021-08-13T19:20:41Z"
    #             }
    #         },
    #         {
    #             "kind": "youtube#searchResult",
    #             "etag": "vynE-kT9KU8Vs68oDiFOrzPDbzY",
    #             "id": {
    #                 "kind": "youtube#video",
    #                 "videoId": "FsNzPscWpOE"
    #             },
    #             "snippet": {
    #                 "publishedAt": "2021-08-12T17:01:07Z",
    #                 "channelId": "UCXDKyqRyXEDQAEIUi5nYFNg",
    #                 "title":"Build a Backend Rest API  with Django REST framework complete tutorial part 2","description": "hi django developers, this is a Django rest framework For Beginners, in this video you will learn what an Api is , how to consume ...",
    #                 "thumbnails": {
    #                     "default": {
    #                         "url": "https://i.ytimg.com/vi/FsNzPscWpOE/default.jpg",
    #                         "width": 120,
    #                         "height": 90
    #                     },
    #                     "medium": {
    #                         "url": "https://i.ytimg.com/vi/FsNzPscWpOE/mqdefault.jpg",
    #                         "width": 320,
    #                         "height": 180
    #                     },
    #                     "high": {
    #                         "url": "https://i.ytimg.com/vi/FsNzPscWpOE/hqdefault.jpg",
    #                         "width": 480,
    #                         "height": 360
    #                     }
    #                 },
    #                 "channelTitle": "Henry Coding stack",
    #                 "liveBroadcastContent": "none",
    #                 "publishTime": "2021-08-12T17:01:07Z"
    #             }
    #         },
    #         {
    #             "kind": "youtube#searchResult",
    #             "etag": "J76_QIVIuw28ly22xc8SuKcdais",
    #             "id": {
    #                 "kind": "youtube#video",
    #                 "videoId": "UAFEoFo_1pE"
    #             },
    #             "snippet": {
    #                 "publishedAt": "2021-08-12T10:23:26Z",
    #                 "channelId": "UCXDKyqRyXEDQAEIUi5nYFNg",
    #                 "title": "Build a Backend Rest API with Django REST framework Complete Tutorial",
    #                 "description":"hi django developers, this is a Django rest framework For Beginners, in this video you will learn what an Api is , how to consume ...","thumbnails": {
    #                     "default": {
    #                         "url": "https://i.ytimg.com/vi/UAFEoFo_1pE/default.jpg",
    #                         "width": 120,
    #                         "height": 90
    #                     },
    #                     "medium": {
    #                         "url": "https://i.ytimg.com/vi/UAFEoFo_1pE/mqdefault.jpg",
    #                         "width": 320,
    #                         "height": 180
    #                     },
    #                     "high": {
    #                         "url": "https://i.ytimg.com/vi/UAFEoFo_1pE/hqdefault.jpg",
    #                         "width": 480,
    #                         "height": 360
    #                     }
    #                 },
    #                 "channelTitle": "Henry Coding stack",
    #                 "liveBroadcastContent": "none",
    #                 "publishTime": "2021-08-12T10:23:26Z"
    #             }
    #         }
    #     ]

    #print(json_data[0]["id"]["videoId"])

    json_data = data.json()["items"]

    ite = 1

    score_list = []

    for video in json_data:
        #print("Iteration : "+ str(ite))
        score = int(videoscore(video["id"]["videoId"]))
        if score != 0:
            score_list.append(score)
        ite += 1


    #avg = total/len(score_list)

    percentage = (sum(score_list) / (len(score_list) * 100)) * 100

    return ({"op_percentage": percentage})

    #print("Your Optimization Score is : "+ str(percentage) + " %")
    