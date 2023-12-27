from pyrogram import Client

api_id = 25836645
api_hash = "7de191651c0201f19bb1451e3b64e5ab"

app = Client("AMinbot", api_id=api_id, api_hash=api_hash)

async def main():
    async with app:
        await app.send_message("me", "Hi!")


app.run(main())