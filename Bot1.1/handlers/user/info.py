import logging
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from loader import dp, bot
from .menu import info
from filters import IsUser

fil1 = "Аэровокзальная, 1г"
fil2 = "Дмитрия Мартынова, 24"


@dp.message_handler(IsUser(), text=info)
async def process_catalog(message: Message):
    markup = InlineKeyboardMarkup(selective=True)
    markup.add(InlineKeyboardButton(fil1, callback_data="aero"))
    markup.add(InlineKeyboardButton(fil2, callback_data="dm"))
    await message.answer("Выберите филиал:", reply_markup=markup)
    

@dp.callback_query_handler(IsUser(), text="aero")
async def show_aero(query: CallbackQuery):
    await bot.send_location(query.message.chat.id, latitude=56.027278, longitude=92.907701)


@dp.callback_query_handler(IsUser(), text="dm")
async def show_aero(query: CallbackQuery):
    await bot.send_location(query.message.chat.id, latitude=56.039531, longitude=92.872474)