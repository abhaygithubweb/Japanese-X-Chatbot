

import random
from datetime import datetime

from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardMarkup, Message

from config import OWNER_USERNAME
from JAPANESE import JAPANESE
from JAPANESE.database.chats import add_served_chat
from JAPANESE.database.users import add_served_user
from JAPANESE.modules.helpers import PNG_BTN


#----------------IMG-------------#



# Random Start Images
IMG = [
    "https://graph.org/file/23aba52acf595658e3937.jpg",
    "https://graph.org/file/184ea2fa773b3483c276e.jpg",
    "https://graph.org/file/d922933fce752cc2ebc13.jpg",
    "https://graph.org/file/6521cddcefbfab9a234f5.jpg",
    "https://graph.org/file/3a1c084b87aaafc42738a.jpg",
    "https://graph.org/file/22d4b65c5ec9f82242698.jpg",
    "https://graph.org/file/5255c32a255069923a9de.jpg",
    "https://graph.org/file/b7b0f16c9ac989b0e190e.jpg",
    "https://graph.org/file/e74fb7feb6fb69941dfb0.jpg",
    "https://graph.org/file/26794ac3dca77479409da.jpg",
    "https://graph.org/file/02c69572b58d6a0c1ef74.jpg",
    "https://graph.org/file/c86bf1b904a714294f2e2.jpg",
    "https://graph.org/file/92983c6ad6bb2867ace33.jpg",
    "https://graph.org/file/b303067a44caf3d7792e9.jpg",
]


#----------------IMG-------------#

#---------------STICKERS---------------#

# Random Stickers
STICKER = [
    "CAACAgUAAx0CYlaJawABBy4vZaieO6T-Ayg3mD-JP-f0yxJngIkAAv0JAALVS_FWQY7kbQSaI-geBA",
    "CAACAgUAAx0CYlaJawABBy4rZaid77Tf70SV_CfjmbMgdJyVD8sAApwLAALGXCFXmCx8ZC5nlfQeBA",
    "CAACAgUAAxkBAAITTWXp4AlCR--xsKQH3PF7dybn2colAAIlCQADHjlVvS9KhV875cQ0BA",
    "CAACAgUAAxkBAAITUWXp4UH70YXnlZ5P6fROnm3PkJDrAAL9CAACi4UhVWaVc1ynp8pcNAQ",
    "CAACAgUAAx0CYlaJawABBy4jZaidvIXNPYnpAjNnKgzaHmh3cvoAAiwIAAIda2lVNdNI2QABHuVVHgQ",
]

#---------------STICKERS---------------#



@JAPANESE.on_cmd("ping")
async def ping(_, message: Message):
    await message.reply_sticker(sticker=random.choice(STICKER))
    start = datetime.now()
    loda = await message.reply_photo(
        photo=random.choice(IMG),
        caption="ᴘɪɴɢɪɴɢ...",
    )
    try:
        await message.delete()
    except:
        pass

    ms = (datetime.now() - start).microseconds / 1000
    await loda.edit_text(
        text=f"нey вαву!!\n{JAPANESE.name} ιѕ alιve 🥀 αnd worĸιng ғιne wιтн a pιng oғ\n➥ `{ms}` ms\n\n<b>|| мαdє ωιтн ❣️ ву [NOBITA_XD❣️](https://t.me/{OWNER_USERNAME}) ||</b>",
        reply_markup=InlineKeyboardMarkup(PNG_BTN),
    )
    if message.chat.type == ChatType.PRIVATE:
        await add_served_user(message.from_user.id)
    else:
        await add_served_chat(message.chat.id)
