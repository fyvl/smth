from aiogram.types import Message
from loader import dp, db
from handlers.user.menu import orders
from filters import IsAdmin

from aiogram.types import Message
from loader import dp, db
from handlers.user.menu import orders
from filters import IsAdmin


@dp.message_handler(IsAdmin(), text=orders)
async def process_orders(message: Message):

    orders = db.fetchall(
        "select usr_name, usr_address, products, title, tag from orders join products"
    )

    if len(orders) == 0:
        await message.answer("У вас нет заказов.")
    else:
        await order_answer(message, orders)


async def order_answer(message, orders):

    res = ""
    c = 1
    for order in orders:
        key = order[2]
        part1, part2 = key.split("=")

        res += (
            f"Заказ: <b>№{c}</b>\nимя лоха: <b>{order[0]}</b>\nадрес лоха: <b>{order[1]}</b>\n"
            f"Категория: <b>{order[4]}</b>\nНазвание: <b>{order[3]}</b>\nКоличество: <b>{part2}</b>\n\n"
        )
        c += 1

    await message.answer(res)
