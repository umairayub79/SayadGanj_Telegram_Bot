from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from constants.bot_messages import SUB_CHANNEL_NAME, SUB_CHANNEL_LINK, INLINE_SEARCH_TITLE
from constants.bot_messages import (
    BOT_USERS,
    SEND_PUBLIC_MESSAGE,
    SEND_PRIVATE_MESSAGE,
    BOT_USERS_CD,
    PUBLIC_MESSAGE,
    PRIVATE_MESSAGE,
    EXIT,
    EXIT_BUTTON_DATA,
    CANCEL,
    )

JOIN_TO_CHANNEL_KEYBOARD = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(SUB_CHANNEL_NAME, url=SUB_CHANNEL_LINK)]
    ]
    )

# Inline keyboard button
INLINE_SEARCH_BUTTON = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(INLINE_SEARCH_TITLE, switch_inline_query="")],
    ]
    )

CANCEL_KEYBOARD = ReplyKeyboardMarkup(
    [
        [KeyboardButton(CANCEL)]
    ],
    resize_keyboard=True
)

ADMIN_OPTIONS = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(BOT_USERS, callback_data=BOT_USERS_CD)],
        [
            InlineKeyboardButton(SEND_PUBLIC_MESSAGE, callback_data=PUBLIC_MESSAGE),
            InlineKeyboardButton(SEND_PRIVATE_MESSAGE, callback_data=PRIVATE_MESSAGE)
        ],
        [InlineKeyboardButton(EXIT, callback_data=EXIT_BUTTON_DATA)]
    ]
)
