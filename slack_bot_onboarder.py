import os
import logging
from flask import Flask
from slack import WebClient
from slackeventsapi import SlackEventAdapter
from slack_bot import SlackBot


app = Flask(__name__)
slack_events_adapter = SlackEventAdapter(os.environ.get("SLACK_EVENTS_TOKEN"), "/slack/events", app)
slack_web_client = WebClient(token=os.environ.get("SLACK_TOKEN"))

def flip_coin(channel):

    coin_bot = SlackBot(channel)
    message = coin_bot.get_message_payload()
    slack_web_client.chat_postMessage(**message)


@slack_events_adapter.on("message")
def message(payload):
    """Parse the message event, and if the activation string is in the text,
    simulate a coin flip and send the result.
    """

    event = payload.get("event", {})
    text = event.get("text")

    if "hey bot" in text.lower():
        channel_id = event.get("channel")
        return flip_coin(channel_id)

if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
    app.run(host='0.0.0.0', port=8080)