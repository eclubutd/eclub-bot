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
                    f'Hey <@{self.member_id}> :wave::skin-tone-5:\n\n'

                    f"We just wanted to send you a final reminder that our *Spring Kickoff* is today from _7:00-8:00 PM_ :hourglass: We know there are so many Zoom/Teams events right now :yawning_face: and we'd all rather be at Blackstone Launchpad, but our team would love to see you tonight even if you can only attend for a few minutes! \n\n "

                    f"You will get to meet other members through our icebreaker, get a brief rundown of our exciting Spring events/projects, ways for you to get involved, provide feedback of what you'd like to see from us, and meet our new officers!\n\n"
                    f">RSVP on Startup Tree <https://utdallas.startuptree.co/event/s/6S8m9ocpVnbC9hLymDK4vS/E-Club-Spring-Kickoff| here>\n"
                    f">MSFT Teams: Join <https://bit.ly/3arpmkC| here>\n\n"

                    f"See you there! :dancing_pikachu:  - E-Club Team "

            )

            }

        }

        super().__init__(member_id, message=EVENT_MSG)


                                    
