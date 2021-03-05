import repackage
repackage.up()

from config import creds
from messages import EventMessage

client = creds.connect_slack()
members = client.users_list()['members']
bots = ['polly', 'eclub_bot', 'slackbot', 'motivation']

for member in members:
    print(member.get('name'), member.get('id'))

'''
for member in members:
    if(member['name'] not in bots):
        print(f"just sent message to: {member.get('name')}")
        kickoff = EventMessage(member_id = member['id'])
        kickoff_msg  = kickoff.get_message()
        response = client.chat_postMessage(**kickoff_msg)
'''

#kickoff = EventMessage(member_id = 'U01J2E488TW')
#kickoff_msg = kickoff.get_message()
#response = client.chat_postMessage(**kickoff_msg)

#member_ids = [member['id'] for member in members]
#print(len(member_ids))
#for id in member_ids:
