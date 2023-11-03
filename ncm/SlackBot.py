import sys
import slack
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask
from slackeventsapi import SlackEventAdapter

#env_path = Path('.') / '.env'
#load_dotenv(dotenv_path=env_path)

#app = Flask(__name__)
#slack_event_adapter = SlackEventAdapter(slack.WebClient(token = os.environ['SIGNING_SECRET']),'/slack/events', app)

#client = slack.WebClient(token = os.environ['SLACK_TOKEN'])
#client.chat_postMessage(channel='#music-sync-automation', text = "Hello! Enter the NetEase URL to get started")
sys.path.append('C:\\Users\\Admin\\UyghurMan\\')

#!/usr/bin/env python
from ncm.start import main
import ncm.config as ncm_config


link =  "https://music.163.com/#/song?id=2021768907"
test = link.rsplit('=')
song_id = test[1]

desired_name = "Song-1"
try:
    download_dir = "C:\\Users\\Admin\\.ncm\\download"
    ncm_config.DOWNLOAD_DIR = download_dir
except:
    print("Unable")

args = ['-s', str(song_id)]
main(args, custom_name = desired_name)


#if __name__ == "__main__":
    #app.run(debug=True)