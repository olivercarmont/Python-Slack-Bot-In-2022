import slack
import os
from dotenv import load_dotenv
from datetime import date
import time

env_path = '.env'
load_dotenv(env_path)

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)

client = slack.WebClient(os.environ['SLACK_BOT_TOKEN'])

client.chat_postMessage(channel="#test-channel", text="The current date is " + str(date.today()) + " " + str(current_time))
