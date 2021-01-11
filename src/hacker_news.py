import requests
from bs4 import BeautifulSoup
from pprint import pprint

response = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty")

limit = 4
top_stories = response.json()[:limit]

# print()

# for story in top_stories:
#     url = f'https://hacker-news.firebaseio.com/v0/item/{story}.json?print=pretty'
#     response = requests.get(url).json()
#     if(response['type'] == "story"):
#         print(response['title'])
#         print(response['url'])
#         print('\n')