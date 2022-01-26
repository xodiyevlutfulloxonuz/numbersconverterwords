import asyncpg
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp, db, bot
from keyboards.inline.inlinekeyboard import keyboards
from states.User import Lang
from aiogram.dispatcher.storage import FSMContext
from data.config import ADMINS
from aiogram.dispatcher.filters.builtin import Command 


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
     users=await db.select_all_users()
     await message.answer(f"Assalomu alaykum, {message.from_user.full_name}! Tilni tanlang.",reply_markup=keyboards)
     await Lang.lang.set()
        
     isHaveUser=True 
        
     for element in users:
         if element[3]==message.from_user.id:
            isHaveUser=False 
            
    
     if isHaveUser==True:
         user = await db.add_user(telegram_id=message.from_user.id,
                                 full_name=message.from_user.full_name,
                                 username=message.from_user.username)

             
     user = await db.select_user(telegram_id=message.from_user.id)
     

     # ADMINGA xabar beramiz
     count = await db.count_users()

     msg = f"{user[1]} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
     await bot.send_message(chat_id=ADMINS[0], text=msg)


