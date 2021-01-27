import creds

client = creds.connect_slack()

class DirectMessage:
    def __init__(self, member_id, message):
        self.member_id = member_id
        self.message = message

    def send_message(self):
        client.chat_postMessage(
                channel = self.member_id,
                text = self.message)



class NewMemberMessage(DirectMessage):

    def __init__(self, member_id): 
        self.member_id = member_id

        WELCOME_MSG = {
            'type': 'section',
            'text':{
                'type':'mrkdwn',
                'text': (
                    f'*Welcome* :wave::skin-tone-6:\n'

                    f"""Hello <@{self.member_id}>! Welcome to the UT Dallas Entrepreneurship Club :bulb """
                )

            }

        }

        super().__init__(member_id,message=WELCOME_MSG)
                                    
                                    
                                    
if __name__ == "__main__":         
    message = NewMemberMessage(member_id='U01HWGD70SE')
    message.send_message()         
                                    
                                   
                                    
                                    
                                   
                                    
                                    
