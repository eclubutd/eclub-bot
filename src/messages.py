import creds

client = creds.connect_slack()

class DirectMessage:
    def __init__(self, member_id, message):
        self.member_id = member_id
        self.message = message
        self.DIVIDER = {'type': 'divider'}


    def get_message(self):
        return {
                'channel': self.member_id,
                'blocks': [
                    self.message,
                    self.DIVIDER
                ]
                }

class NewMemberMessage(DirectMessage):

    def __init__(self, member_id): 
        self.member_id = member_id

        WELCOME_MSG = {
                'type': 'section',
                'text':{
                    'type':'mrkdwn',
                    'text': (
                        f'*Welcome* :wave::skin-tone-6:\n\n'

                        f"""Hello <@{self.member_id}>! Welcome to the UT Dallas Entrepreneurship Club :bulb: We are a premier student organization focused on building a community of student builders, founders, and aspiring entrepreneurs. Thanks for joining us on your journey!\n\n"""
                        
                        
                        f"_*Spring 2021 Member Checklist*_ :memo:\n We have just five easy steps (~ few minutes) for you to become a full member! We do not currently collect any :money_with_wings: or any of that, but we do ask that you complete the following to stay up to date with our growing community\n\n"
                        f"*Steps:*\n"
                        f"1. Introduce yourself in the #intros channel in our slack! We'd love for to know your major, classification, experience, and why you are interested in entrepreneurship\n"
                        f"2. Join our Microsoft Teams Channel: this is where we will host all our events and event postings. Register <https://bit.ly/39ZZE6o | here>\n"
                        f"3. Sign up for our bi-weekly email newsletter: We post hiring opportunities, competitions, events, startup/tech/venture content! Sign up <https://bit.ly/3ablcNP | here>\n"
                        f"4. Follow us on Instagram: It is our most activate social media! But we have a <https://www.facebook.com/UTDEclub | Facebook> as well. Click <https://www.instagram.com/eclubutd/| here> for Instagram\n"
                        f"5. Join UT Dallas Startup Tree: the central hub for all things entrepreneurship at UTD (mentors, events, job fairs, mentors, and more) Sign up <https://utdallas.startuptree.co/ | here>\n\n"

                        f":zap: _*Two important resources:*_ :zap: \n"
                        f"<https://www.notion.so/UTD-Entrepreneurship-Club-aa275bd8631344729835b39f895ab56e| Member Notion>\n"
                        f"<https://www.eclubutd.com | Revamped and improved website>\n\n"

                        f">There are more slacks then the ones shown by default. Please feel free to make your own here (<https://www.notion.so/E-Club-Slack-Channel-Guide-649dff0ac5e34430b6092cbe5fd3ecb2 | Channel guide>)\n\n"

                        f"Again, thank you for joining us! Let's build and grow :rocket: - E-Club Team "
                    )
            }

        }

        super().__init__(member_id,message=WELCOME_MSG)
                                    
                                    
                                    
                                   
class EventMessage(DirectMessage):
    def __init__(self, member_id):
        self.member_id = member_id


        EVENT_MSG = {
            'type': 'section',
            'text': {
                'type':'mrkdwn',
                'text':(
                    f'Hey <@{self.member_id}>! We just wanted to remind you that we are having our Personal Branding 101 Event right now! till 8 PM CST\n\n'

                    f"The speaker is <https://www.linkedin.com/in/emchvn|Emily Chan> who is co-founder of Sparkline and a talent sourcer at Microsoft! She is talking about the importance of personal branding in one's professional life.\n\nThere will also be a Q&A session after that!!!\n\n"
                    f">MSFT Teams: Join <https://teams.microsoft.com/l/meetup-join/19%3a717c7166782b45809a38cc5386a05f6f%40thread.tacv2/1611456140026?context=%7b%22Tid%22%3a%228d281d1d-9c4d-4bf7-b16e-032d15de9f6c%22%2c%22Oid%22%3a%22875bf001-5804-4c00-86ae-47f481ceaa18%22%7d| here>\n\n"

            )

            }

        }

        super().__init__(member_id, message=EVENT_MSG)


                                    
