
from  dotenv import load_dotenv, find_dotenv
from slack import WebClient
import os

#find_dotenv() return absolute path of .env file in project and reads the key,value pair from .env and adds them to environment variable.
load_dotenv(find_dotenv())

def connect_slack():
    return WebClient(token=os.environ['SLACK_API_TOKEN'])

def get_smmry_key():
    return os.environ['SMMRY_API_KEY']

def get_slack_test_webhook_url():
    return os.environ['SLACK_TEST_WEBHOOK_URL']