from telethon.sessions import StringSession
from telethon.sync import TelegramClient


print("""Goto my.telegram.org and get api id and api hash""")


API_ID = int(input("Enter API ID : "))
API_HASH = input("Enter API HASH : ")

with TelegramClient(StringSession(), API_ID, API_HASH) as client:
    print(client.session.save())
    client.send_message("me", client.session.save())

print("This String session has been saved in 'saved messages' in your account.")
