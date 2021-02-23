from bs4 import BeautifulSoup
from datetime import datetime, date, timedelta
from pprint import pprint
import creds
import requests

# REMEMBER: this only works on weekdays (TC does not produce articles on Sat/Sun)

class TechCrunch:
  def __init__(self, num_articles = 5):
    self.num_articles = num_articles
    self.startups_url = 'https://techcrunch.com/startups/'

  def scraper(self):
    yesterday_date = str(date.today() - timedelta(days = 1))
    try:
      r = requests.get(self.startups_url)
      r.raise_for_status()
    except requests.exceptions.HTTPError as errh:
      print ("Http Error:",errh)
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:",errc)
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:",errt)
    except requests.exceptions.RequestException as err:
        print ("Oops: Something Else",err)

    soup = BeautifulSoup(r.content, 'lxml')

    root_div = soup.find('div', attrs = {'class': 'content'})
    headers = root_div.find_all('header', attrs = {'class': 'post-block__header'})

    
    articles = {}

    count = 0
    for header in headers:
      article_date = header.find('time')['datetime'].split('T')[0]
      print(article_date)
      if(article_date == yesterday_date and count < self.num_articles):
        article = header.h2.a
        title = article.text.strip()
        link = article.get('href').strip()
        articles[title] = {}
        articles[title]['link'] = link
        articles[title]['summary'] = self.summarize_article(link)
        count+=1
      
    return articles

  def summarize_article(self, url: str) -> str:
    """ using the summary api """
    SMMRY_API_URL = 'https://api.smmry.com'

    params = {
      'SM_API_KEY': creds.get_smmry_key(),
      'SM_LENGTH': 1, 
      'SM_IGNORE_LENGTH': True,
      'SM_URL': url,
      }

    response = requests.get(SMMRY_API_URL, params = params).json()

    #TODO: check here (try-catch)
    summary = response['sm_api_content'].strip()
    return summary

if __name__ == "__main__":
  tc = TechCrunch()
  pprint(tc.scraper())
