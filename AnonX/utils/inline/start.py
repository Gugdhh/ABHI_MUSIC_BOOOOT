from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="ð¤ á´á´á´ á´á´ á´á´ Êá´á´Ê É¢Êá´á´á´ ð¤",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="ð Êá´Êá´© ð",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="sá´á´á´ÉªÉ´É¢s", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="ð¤ á´á´á´ á´á´ á´á´ Êá´á´Ê É¢Êá´á´á´ ð¤",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="ð Êá´Êá´© ð", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="â sá´á´©á´©á´Êá´ â", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="ð á´É´á´á´ ð", user_id=OWNER
            )
        ],
     ]
    return buttons
