import creds
from messages import EventMessage

client = creds.connect_slack()
members = client.users_list()['members']

print(len(members))

bots = ['polly', 'eclub_bot', 'slackbot', 'motivation']

"""
for member in members:
    if(member['name'] not in bots):
        kickoff = EventMessage(member_id = member['id'])
        kickoff_msg  = kickoff.get_message()
        response = client.chat_postMessage(**kickoff_msg)
    else:
        pass
"""

message = EventMessage(member_id = 'U01KX0JJZGQ')
message_msg = message.get_message()
response = client.chat_postMessage(**message_msg)


#member_ids = [member['id'] for member in members]
#print(len(member_ids))
#for id in member_ids:
