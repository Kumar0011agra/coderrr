from pyrogram.types import InlineKeyboardButton

import config
from Spotify_Music import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(text=" ᴀᴅᴅ ᴍᴇ ᴛᴏ ɢʀᴏᴜᴘ ", url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(text=" ʜᴇʟᴘ ", callback_data="settings_back_helper"),
            InlineKeyboardButton(
                text=" sᴇᴛ ", callback_data="settings_helper"
            ),
        ],
      [
             InlineKeyboardButton(text=" 🗑️ ", callback_data="close"),
    ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(text=" ʜᴇʟᴘ ", callback_data="settings_back_helper"),
            InlineKeyboardButton(text=" 『ɪɴᴅ』乛 𝐃𝚲꯭𝗥𝚱 ִֶָ 𝐂❍𝐃𝜩Ɽ𓍢ִ໋🍃‌֒ ִֶָ 𝅃꯭᳚𓆩꯭〭〬🤍𓆪ꪾ ", url=f"https://t.me/@MR_CODER_DARK"),
            ],
                    [
                    InlineKeyboardButton(text=" ᴀᴅᴅ ᴍᴇ ᴛᴏ ɢʀᴏᴜᴘ ", url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text=_["S_B_7"], callback_data="gib_source"),
             InlineKeyboardButton(text=" 🗑️ ", callback_data="close"),
    ],
    ]
    return buttons
    
    
