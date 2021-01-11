from flask import Flask
from config import creds
from slack.errors import SlackApiError
from slackeventsapi import SlackEventAdapter
import os
from pprint import pprint
import time

app = Flask(__name__)
client = creds.connect_slack()

#requests will go to a public ip + /slack/events
slack_events_adapter = SlackEventAdapter(
    os.environ['SLACK_SIGNING_SECRET'], '/slack/events', app)


@app.route('/')
def hello():
  return "Hello World"

if __name__ == "__main__":
  app.run(debug=True, port=7000)