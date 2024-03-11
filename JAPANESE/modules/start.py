

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
    "https://graph.org/file/006664da757b3f2bfb8f6.jpg",
    "https://graph.org/file/a41ae45d67020b33a7b47.jpg",
    "https://graph.org/file/d47e114d21b23be75dad9.jpg",
    "https://graph.org/file/43e06529a34ab16233dec.jpg",
    "https://graph.org/file/c9de628c5365a508b6b5b.jpg",
    "https://graph.org/file/807e296176fc44e523072.jpg",
    "https://graph.org/file/b57a354abba72c1c9eab5.jpg",
    "https://graph.org/file/0f5f08d9927849b8da3fa.jpg",
    "https://graph.org/file/9fa608bd538a804244c02.jpg",
    "https://graph.org/file/84d6d5e53ed97656f8fb9.jpg",
    "https://graph.org/file/b1474e7522222563c1095.jpg",
    "https://graph.org/file/a455762865a81bac12f1c.jpg",
    "https://graph.org/file/194e0f43501f1fec44bbb.jpg",
    "https://graph.org/file/02c607ba5bff48cbffb7a.jpg",
    "https://graph.org/file/6edece8fed906ae0fb5f4.jpg",
    "https://graph.org/file/facdefe99c646a095cf8b.jpg",
    "https://graph.org/file/08387602c7ed3a86bad8e.jpg",
    "https://graph.org/file/84b3c23982f765fefc898.jpg",
    "https://graph.org/file/4af570c30ed1378f332b1.jpg",
    "https://graph.org/file/366946ca38e24dd57b6c4.jpg",
    "https://graph.org/file/979069f0620e5fca80710.jpg",
    "https://graph.org/file/3878f96e3a6121d872ef8.jpg",
    "https://graph.org/file/b2dff174e6e614912536c.jpg",
    "https://graph.org/file/5f6221368d66f1cdd5473.jpg",
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
