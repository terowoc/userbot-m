from pyrogram import Client
from bios import Bio
from pyrogram import enums

api_id = 25836645
api_hash = "7de191651c0201f19bb1451e3b64e5ab"

app = Client("AMinbot", api_id=api_id, api_hash=api_hash)
bio = Bio.get_bio()

async def main():
    async with app:
        if file == 0:
            await app.update_profile(bio=bio)
            # profile.txt -> 1
            # 60 -> profile.txt -> 0
        
app.run(main())