

import asyncio
import random

from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardMarkup, Message


from JAPANESE import JAPANESE
from JAPANESE.database.chats import add_served_chat
from JAPANESE.database.users import add_served_user
from JAPANESE.modules.helpers import (
    CLOSE_BTN,
    DEV_OP,
    HELP_BTN,
    HELP_BUTN,
    HELP_READ,
    HELP_START,
    SOURCE_READ,
    START,
)


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
    "CAACAgUAAxkBAAITX2Xp5TMUDAWPjWiN8EZyJkWM-RARAAK0CQACqQ_5V-RZJbz6rcugNAQ",
    "CAACAgUAAxkBAAITYWXp5VNZWEH8IMbp9ajdAaV-rGGSAAL5CAACxBP5V7A-_Lnh2wMfNAQ",
    "CAACAgUAAxkBAAITTWXp4AlCR--xsKQH3PF7dybn2colAAIlCQADHjlVvS9KhV875cQ0BA",
    "CAACAgUAAxkBAAITUWXp4UH70YXnlZ5P6fROnm3PkJDrAAL9CAACi4UhVWaVc1ynp8pcNAQ",
    "CAACAgUAAxkBAAITU2Xp4kqciZiY_91FfGVAT_KTj2s9AAJnCAAC6AcpVieAF92a58u7NAQ",
    "CAACAgUAAxkBAAITVWXp4lKRRMg3y1j3N2wzmceBLtsmAAJ-CQACZkMoVufDmrteA1zNNAQ",
    "CAACAgUAAxkBAAITV2Xp4lVGe4GCPFQGgeIZ28pnB8nNAAKmCAACUZkpVnUNiOQhHoe8NAQ",
    "CAACAgUAAxkBAAITWWXp5FLmat3VWn0KhkQbu35Y-thvAAJACAACIk35V6aZ2AESsH3bNAQ",
    "CAACAgUAAxkBAAITW2Xp5FrAcUwSzUHaEPRmRkxWSUorAAJrCAAC7HsBVJHGZr9K3pXtNAQ",
    "CAACAgUAAxkBAAITYWXp5VNZWEH8IMbp9ajdAaV-rGGSAAL5CAACxBP5V7A-_Lnh2wMfNAQ",
    "CAACAgUAAxkBAAITY2Xp52m17BcwJqVcPsl384f3dLzWAAIaBwACT6uxVB5i5IhDUemeNAQ",
    "CAACAgUAAxkBAAITZWXp523e5IxlezWWZ2wF6tYuOMQCAAISBgACV3GxVMDUxf3w_6e4NAQ",
    "CAACAgUAAxkBAAITZ2Xp528boFk0dRZiSFPOghEu-leMAAL0BgACbNKpVOzvOyOVKqlPNAQ",
    "CAACAgQAAxkBAAITaWXp53Q_3z_rzJjXsNXEDqxw2poIAAJ3CgACQ1fYU6bJbC6o_pLANAQ",
    "CAACAgQAAxkBAAITa2Xp53niiOvQiDwcgT_mtcyBj_HqAAKSDgAClgbZUyP5wv8DXGD6NAQ",
    "CAACAgQAAxkBAAITbWXp54LbnDE3IEPiv5ouR2-w_xf6AAIaDAACSLLZU0eGtzZ3gIG1NAQ",
    "CAACAgQAAxkBAAITb2Xp54McvMTIs3WR1Vo8LDy22jWbAAIUDAACqAAB2FPkrLoMDb63VjQE",
    "CAACAgQAAxkBAAITcWXp54aH2p6u2it55Kf2V0JQKc95AAJuCgACGXvQU1cCgM17P_uhNAQ",
    "CAACAgQAAxkBAAITc2Xp54kkKq1QpyUNFW9HMwwPtyPGAAITCQACytDRU6OQesPECnYtNAQ",
    "CAACAgQAAxkBAAITdWXp54yTwicLk0m_q1knqZJHEHsbAAIfDgAChlnRUxG5W8JC35m3NAQ",
    "CAACAgQAAxkBAAITd2Xp542NEDO3SQ1_bqv8ffyVMvKnAAIwCwACJxbRUymWwxmdNfZ7NAQ",
    "CAACAgQAAxkBAAITeWXp55Dq7OgzCLBmA6GaORKf3IlOAAIPDQACM0MZUMhzwSREqiDXNAQ",
]

#---------------STICKERS---------------#


#---------------EMOJIOS---------------#

EMOJIOS = [
    "💣",
    "💥",
    "🪄",
    "❤️",
    "💀",
    "🥀",
    "🔥",
    "🧨",
    "⚡",
    "🤡",
    "👻",
    "🎃",
    "🎩",
    "🕊",
]


#---------------EMOJIOS---------------#

@JAPANESE.on_cmd(["start", "aistart"])
async def start(_, m: Message):
    if m.chat.type == ChatType.PRIVATE:
        accha = await m.reply_text(
            text=random.choice(EMOJIOS),
        )
        await asyncio.sleep(1.3)
        await accha.edit("__ᴅιиg ᴅσиg ꨄ︎ ѕтαятιиg..__")
        await asyncio.sleep(0.2)
        await accha.edit("__ᴅιиg ᴅσиg ꨄ sтαятιиg.....__")
        await asyncio.sleep(0.2)
        await accha.edit("__ᴅιиg ᴅσиg ꨄ︎ sтαятιиg..__")
        await asyncio.sleep(0.2)
        await accha.delete()
        umm = await m.reply_sticker(sticker=random.choice(STICKER))
        await asyncio.sleep(2)
        await umm.delete()
        await m.reply_photo(
            photo=random.choice(IMG),
            caption=f"""**๏ ʜᴇʏ, ɪ ᴀᴍ {JAPANESE.name}**\n**➻ ᴀɴ ᴀɪ ʙᴀsᴇᴅ ᴄʜᴀᴛʙᴏᴛ.**\n**──────────────**\n**➻ ᴜsᴀɢᴇ /chatbot [ᴏɴ/ᴏғғ]**\n<b>||๏ ʜɪᴛ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ғᴏʀ ʜᴇʟᴘ||</b>""",
            reply_markup=InlineKeyboardMarkup(DEV_OP),
        )
        await add_served_user(m.from_user.id)
    else:
        await m.reply_photo(
            photo=random.choice(IMG),
            caption=START,
            reply_markup=InlineKeyboardMarkup(HELP_START),
        )
        await add_served_chat(m.chat.id)


@JAPANESE.on_cmd("help")
async def help(client: JAPANESE, m: Message):
    if m.chat.type == ChatType.PRIVATE:
        hmm = await m.reply_photo(
            photo=random.choice(IMG),
            caption=HELP_READ,
            reply_markup=InlineKeyboardMarkup(HELP_BTN),
        )
        await add_served_user(m.from_user.id)
    else:
        await m.reply_photo(
            photo=random.choice(IMG),
            caption="**ʜᴇʏ, ᴘᴍ ᴍᴇ ғᴏʀ ʜᴇʟᴘ ᴄᴏᴍᴍᴀɴᴅs!**",
            reply_markup=InlineKeyboardMarkup(HELP_BUTN),
        )
        await add_served_chat(m.chat.id)


@JAPANESE.on_cmd("repo")
async def repo(_, m: Message):
    await m.reply_text(
        text=SOURCE_READ,
        reply_markup=InlineKeyboardMarkup(CLOSE_BTN),
        disable_web_page_preview=True,
    )


@JAPANESE.on_message(filters.new_chat_members)
async def welcome(_, m: Message):
    for member in m.new_chat_members:
        await m.reply_photo(photo=random.choice(IMG), caption=START)
