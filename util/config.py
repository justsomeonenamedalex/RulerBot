import json
import os
import sys

dir_path = os.path.dirname(os.path.realpath(__file__))
if sys.platform.startswith("linux"):
    config_path = dir_path + "/config.json"
elif sys.platform.startswith("win"):
    config_path = dir_path + "\\config.json"

with open(config_path) as file:
    data = json.load(file)

token = data["BOT_TOKEN"]
prefix = data["BOT_PREFIX"]
activity = data["DEFAULT_ACTIVITY_MESSAGE"]
invite_link = data["INVITE_LINK"]
