import json
import requests
import creds 
from pprint import pprint
from slack.errors import SlackApiError
import logging

logging.basicConfig(
    level=logging.ERROR,
    format="{asctime} {levelname: <8} {message}",
    style="{",
    filename="../logs/slack.log",
    filemode='a'
)

client = creds.connect_slack()

def send_slack_new_member(member_id):
  ''' goal: alert team when new member has joined '''
  
  webhook_url = creds.get_slack_webhook_url(channel = "robots")

  try:
    member_info = client.users_info(user = member_id).get('user').get('profile')
    name = member_info.get('display_name_normalized')
    email = member_info.get('email')

    data = {
      "channel": "test",
        "blocks": [
      {
        "type": "section",
        "text": {
          "type": "mrkdwn",
          "text": (
            f':mega: New Slack Member :mega:\n'
            f"*Name*: {name}\n"
            f'*Email*: {email}'
          )
        }
      },
      {
        "type": "divider"
      },
      {
        "type": "section",
        "text": {
          "type": "mrkdwn",
          "text": "Officer in charge of outreach: "
        },
        "accessory": {
          "type": "users_select",
          "placeholder": {
            "type": "plain_text",
            "text": "Select a user",
            "emoji": True
          },
          "action_id": "users_select-action"
        }
      },
      {
        "type": "section",
        "text": {
          "type": "mrkdwn",
          "text": "Date Reaching Out"
        },
        "accessory": {
          "type": "datepicker",
          "placeholder": {
            "type": "plain_text",
            "text": "Select a date",
            "emoji": True
          },
          "action_id": "datepicker-action"
        }
      },
      {
        "type": "section",
        "text": {
          "type": "mrkdwn",
          "text": "Please check if you have outreached: "
        },
        "accessory": {
          "type": "radio_buttons",
          "options": [
            {
              "text": {
                "type": "plain_text",
                "text": "Yes",
                "emoji": True
              },
              "value": "value-0"
            },
            {
              "text": {
                "type": "plain_text",
                "text": "No",
                "emoji": True
              },
              "value": "value-1"
            }
          ],
          "action_id": "radio_buttons-action"
        }
      }
    ]
    }

    requests.post(
      webhook_url,
      data = json.dumps(data),
      headers = {"Content-Type": "application/json"}
    )
  except SlackApiError as e:
    logger.error("There was an error finding slack user", exc_info)
  except Exception as e:
    logger.error(e)

