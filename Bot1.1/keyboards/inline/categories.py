from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from loader import db

category_cb = CallbackData("category", "id", "action")


def categories_markup():

    global category_cb

    markup = InlineKeyboardMarkup()
    for idx, title, parentID in db.fetchall(
        "SELECT * FROM categories WHERE parentID = 0"
    ):
        markup.add(
            InlineKeyboardButton(
                title, callback_data=category_cb.new(id=idx, action="view")
            )
        )

    return markup


def sub_categories_markup(data):
    global category_cb

    sub_markup = InlineKeyboardMarkup()
    for idx, title, parentID in data:
        sub_markup.add(
            InlineKeyboardButton(
                title, callback_data=category_cb.new(id=idx, action="view")
            )
        )

    return sub_markup
