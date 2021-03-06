from creds import get_airtable_key, connect_slack
from airtable import Airtable
from slack.errors import SlackApiError
import logging

client = connect_slack()

logging.basicConfig(
        level=logging.ERROR,
        format="{asctime} {levelname: <8} {message}",
        style="{",
        filename="../logs/slack.log",
        filemode='a'
        )

class ClubAirtable:
    def __init__(self):
        self.api_key = get_airtable_key()

class CurrentMemberBase(ClubAirtable):
    def __init__(self):
        super().__init__()
        self.base_id = 'appuEYc3owMcgwtNR'
        self.TABLE_NAME = 'Current Members (Slack)'
        self.base = Airtable(self.base_id, self.TABLE_NAME, self.api_key)

    def add_new_member(self, member_id):
        try:
            if(not self.base.search('Slack_id', member_id)):
                member_info = client.users_info(user = member_id).get('user').get('profile')
                name = member_info.get('display_name_normalized')
                email = member_info.get('email')

                self.base.insert({
                    'Slack_id': member_id, 
                    'Name': name,
                    'Email': email
                    })

        except SlackApiError as e:
            logging.error("There was an error finding slack user", exc_info)
        except Exception as e:
            logging.error(e)
