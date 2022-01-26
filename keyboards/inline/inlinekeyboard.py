from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

keyboards = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='English  🇺🇸', callback_data='en'),
        InlineKeyboardButton(text='Russian 🇷🇺', callback_data='ru')],

         [InlineKeyboardButton(text='Korean  🇰🇷', callback_data='ko'),
        InlineKeyboardButton(text='Japan 🇯🇵', callback_data='ja')],
         [InlineKeyboardButton(text='French  🇫🇷', callback_data='fr'),
        InlineKeyboardButton(text='German 🇩🇪', callback_data='de')]
         

    ]
)
