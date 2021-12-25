from aiogram.types import Message, CallbackQuery, ReplyKeyboardMarkup, ContentType
from aiogram.dispatcher import FSMContext
from time import sleep
from aiogram_broadcaster import MessageBroadcaster

from app import menu_message, joinedUsers
from loader import dp, bot
from filters import IsAdmin, IsUser
from states import PostState

catalog = "🛍️ Каталог"
balance = "💰 Баланс"
cart = "🛒 Корзина"
delivery_status = "🚚 Статус заказа"
info = "📄 Наш адрес"

settings = "⚙️ Настройка каталога"
# sub_settings = "⚙️ Настройка подкаталога"
# orders = "🚚 Заказы"
questions = "❓ Вопросы"


@dp.message_handler(IsAdmin(), commands=["admin"])
async def admin_menu(message: Message):
    markup = ReplyKeyboardMarkup(selective=True, resize_keyboard=True)
    markup.add(settings, questions)
    # markup.add(sub_settings, orders)

    await message.answer("Меню", reply_markup=markup)


@dp.message_handler(IsAdmin(), commands=["post"])
async def broadcast_command(message: Message, state: FSMContext):
    await message.answer("Введите текст для начала рассылки:")
    await PostState.text.set()


@dp.message_handler(IsAdmin(), state=PostState.text)
async def broadcast(message: Message, state: FSMContext):
    # for user in joinedUsers:
    #     await bot.send_message(user, message.text)
    tekst = message.text
    textFile = open("text.txt", "a")
    textFile.write(str(tekst) + "\n")
    await PostState.photo.set()


@dp.message_handler(IsAdmin(), content_types=["photo"], state=PostState.photo)
async def broadcast(message: Message, state: FSMContext):
    photo_id = message.photo[-1].file_id
    text_file = open("text.txt", "r")
    lines = text_file.read()
    for user in joinedUsers:
        await bot.send_photo(user, photo_id, caption=lines)
    f = open('text.txt', 'w+')
    f.seek(0)
    f.close()
    await state.finish()


@dp.message_handler(text=menu_message)
async def user_menu(message: Message):
    markup = ReplyKeyboardMarkup(selective=True, resize_keyboard=True)
    markup.add(catalog, cart, info)
    # markup.add(cart)
    # markup.add(delivery_status)

    await message.answer("Меню", reply_markup=markup)


@dp.message_handler(commands=["menu"])
async def user_menu(message: Message):
    markup = ReplyKeyboardMarkup(selective=True, resize_keyboard=True)
    markup.add(catalog, cart, info)

    await message.answer("Меню", reply_markup=markup)
