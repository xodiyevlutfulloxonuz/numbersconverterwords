from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

keyboards = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='English  πΊπΈ', callback_data='en'),
        InlineKeyboardButton(text='Russian π·πΊ', callback_data='ru')],

         [InlineKeyboardButton(text='Korean  π°π·', callback_data='ko'),
        InlineKeyboardButton(text='Japan π―π΅', callback_data='ja')],
         [InlineKeyboardButton(text='French  π«π·', callback_data='fr'),
        InlineKeyboardButton(text='German π©πͺ', callback_data='de')]
         

    ]
)
