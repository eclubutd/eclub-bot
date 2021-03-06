from slack.errors import SlackApiError
from slackeventsapi import SlackEventAdapter
from flask import Flask, request, Response
import creds
from messages import NewMemberMessage
from club_airtable import CurrentMemberBase

import os
from pprint import pprint
import officer_util
import time
import re

app = Flask(__name__)
client = creds.connect_slack()

#requests will go to a public ip + /slack/events
slack_events_adapter = SlackEventAdapter(
    os.environ['SLACK_SIGNING_SECRET'], '/slack/events', app)

@slack_events_adapter.on('member_joined_channel')
def member_join(payload):
    try:
        general_channel_id = 'C01HFP9KMRD'
        event = payload.get('event')
        user_id = event.get('user')
        pprint(user_id)

        channel_id = event.get('channel')
        if(channel_id == general_channel_id):
            new_member  = NewMemberMessage(member_id = user_id)
            msg = new_member.get_message()
            response = client.chat_postMessage(**msg)
            CurrentMemberBase().add_new_member(user_id)
            officer_util.send_slack_new_member(user_id)
    except Exception as e:
        print(e)
  

@slack_events_adapter.on('reaction_added')
def reaction_test(payload):
    pprint(payload)

@app.route('/eclub_newsletter')
def send_newsletter():
    print("received request")


@app.route('/newsletter',methods=['POST'])
def newsletter() -> Response:
  newsletter_re = r"(subscribe|unsubscribe) (slack|email)( '\S@\S+')*"
  payload = request.form
  text = payload.get('text').strip()

  usr_msg = ''
  success_msg = 'We have succesffuly processed your request!'

  if(re.search(newsletter_re, text)):
    arguments = text.split()
    platform = arguments[1]

    if(platform == "email"):
      if(len(arguments) == 3):
        #TODO: subscribe mailchimp
        usr_msg = success_msg
        pass
      else:
        usr_msg = "We couldn't process your request: Please make sure to include your email address"
    else:
      #TODO: handle slack unsubscribes and subscribes
      usr_msg = success_msg
      pass
  else:
    usr_msg = "We couldn't process your request: Make sure you have (action) (platform) (email address if platform is email). /n Example: /newsletter subscribe email Elon.Musk@utdallas.edu"

  client.chat_postEphemeral(
    channel = payload.get('channel_id'),
    user = payload.get('user_id'),
    text = usr_msg)
  return Response(), 200


if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)
