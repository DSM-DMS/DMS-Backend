from slacker import Slacker
import os

slack_token = os.getenv('SLACK_BOT_TOKEN')
slack_bot = Slacker(slack_token)