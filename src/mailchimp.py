import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError
from pprint import pprint
from bs4 import BeautifulSoup 

try:
    client = MailchimpMarketing.Client()
    client.set_config({
        "api_key": "b80d7ce5bd37f1f133f5b4202e16e76e-us8",
        "server": "us8"
        })
    response = client.campaigns.list(sort_field="send_time",sort_dir="DESC", count=2)
    campaign = response['campaigns'][1]
    id = campaign['id']
    
    campaign_html = client.campaigns.get_content(id)['archive_html']
except ApiClientError as error:
    print(error)


soup = BeautifulSoup(campaign_html, 'lxml')
headers = soup.find_all('div',attrs = {'style':"text-align"})
pprint(headers)
pprint(len(headers))


