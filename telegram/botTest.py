import configparser
import json



from telethon import TelegramClient
from telethon.tl.types import InputMessagesFilterPhotos
from telethon.errors import SessionPasswordNeededError


# # Reading Configs
config = configparser.ConfigParser()
config.read("config.ini")
#
# # Setting configuration values
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
#
api_hash = str(api_hash)
#
phone = config['Telegram']['phone']
username = config['Telegram']['username']

# Create the client and connect

client = TelegramClient(username, api_id, api_hash)
group_name = "https://t.me/boolhongchat"

async def main():
    print("Started")
    #message = await client.get_messages(group_name, limit=5)
    #print(message)
    await client.send_message(group_name, "만세!")

with client:
    client.loop.run_until_complete(main())

