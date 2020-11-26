from slack import WebClient
from slack_bot import SlackBot
import os

# Create a slack client
slack_web_client = WebClient(token=os.environ.get("SLACK_TOKEN"))

# Get a new CoinBot
slack_bot = SlackBot("#n")

# Get the onboarding message payload
message = slack_bot.get_message_payload()

# Post the onboarding message in Slack
slack_web_client.chat_postMessage(**message)