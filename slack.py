from slackclient import SlackClient
from slack_token import slack_token
import os

"""
  Instructions:
  Go to https://<slackdomain>.slack.com/apps/A0F7YS25R-bots
  Make a bot by clicking `Add Configuration`, and download the corresponding token
  Create a new file slack_token.py in this directory, with the single line `slack_token = "..."`
"""

def get_slack_ids(usernames):
    client = SlackClient(slack_token)
    users_info = client.api_call("users.list")['members']
    def users_by_name(name):
        return [x['id'] for x in users_info if matches(name, x)]
    by_name = [(name, users_by_name(name)) for name in usernames]
    return {name: ids[0] for name, ids in by_name if ids}

def post_message(slack_ids, text):
    if isinstance(slack_ids, str):
        slack_ids = [slack_ids]
    client = SlackClient(slack_token)
    channel = client.api_call(
        "conversations.open",
        users=slack_ids)['channel']['id']
    result = client.api_call(
       "chat.postMessage",
       channel=channel, text=text, as_user=False,
       username='onuw-bot',
       icon_emoji='robot')
    if 'error' in result:
        print(f'Error slacking: {result}')

def matches(name, user):
    return name.upper() in {x.split()[0].split('.')[0].upper() if x else ''
                            for x in [user['name'], user['profile']['display_name'], user['profile']['real_name']]}
