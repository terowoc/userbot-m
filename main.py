from pyrogram import Client
from bios import Bio
from pyrogram import enums
import time

api_id = 25836645
api_hash = "7de191651c0201f19bb1451e3b64e5ab"

app = Client("AMinbot", api_id=api_id, api_hash=api_hash)
bio = Bio.get_bio()

async def main():
    async with app:
        await app.update_profile(bio=bio)

keywords = [
    'oka',
    'brother'
]

@app.on_message()
async def my_handler(client, message):
    print(message.chat.id)
    
    await app.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    
    print(f"Received message: {message.text}")
    
    # Check if the message text contains any keyword from the keywords list
    if any(keyword.lower() in message.text.lower() for keyword in keywords):
        print("Forwarding message...")
        await message.forward("me")
    else:
        print("Message does not match keywords.")

    main()

app.run()