import asyncio

from Spotify_Music import app
from pyrogram import filters
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from config import MUSIC_BOT_NAME

@app.on_message(filters.command(["repo"]))
async def start(client: Client, message: Message):
    await message.reply_video(
        video=f"https://graph.org/file/dd1b9ef79d2442d2817cd.mp4",
        caption=f"❤️ ʜᴇʏ {message.from_user.mention}",
        reply_markup=InlineKeyboardMarkup(
            [
               [
            InlineKeyboardButton(
                text="☆ ᴏᴡɴᴇʀ 💗 ", url=f"https://t.me/ll_NOBITA_BOT_DEVLOPER_ll"
            ),
            InlineKeyboardButton(
                text="☆ ꜱᴜᴘᴘᴏʀᴛ 💗", url=f"https://t.me/NOBITA_SUPPORT"
            ),
        ],
                [
                    InlineKeyboardButton(
                        "✯ ᴄʟᴏsᴇ ✯", callback_data="close"
                    )
                ],
            ]
        )
    )
  
# donate #
@app.on_message(filters.command(["donate, qr, scanner"]))
async def start(client: Client, message: Message):
    await message.reply_video(
        video=f"https://graph.org/file/0a51a4ab5ac6e11669e76.jpg",
        caption=f"❤️ ʜᴇʏ {message.from_user.mention}",
    )
