from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove,\
    InlineKeyboardMarkup, InlineKeyboardButton
from database import items

main = ReplyKeyboardMarkup(resize_keyboard=True)
main.add('Каталог 👟').add('Корзина 🗑').add('Контакты 📲')

admin_main = ReplyKeyboardMarkup(resize_keyboard=True)
admin_main.add('Каталог 👟').add('Корзина 🗑').add('Контакты 📲').add('Добавить товар')

cancel = ReplyKeyboardMarkup(resize_keyboard=True)
cancel.add('Отмена')

#  ------------------------------------------------------------------
"""
Скрипт создания инлайн кнопок в каталоге с помощью перебора всех имён в БД
"""
buttons = []
for item in items:
    button = InlineKeyboardButton(item[0], callback_data=item[0])
    buttons.append(button)

catalog = InlineKeyboardMarkup(row_width=2)
catalog.add(*buttons)

#  ------------------------------------------------------------------

add_to_cart = InlineKeyboardMarkup(row_width=2)
add_to_cart.add(InlineKeyboardButton('Добавить в корзину', callback_data='add_to_cart'))

buy = InlineKeyboardMarkup(row_width=1)
buy.add(InlineKeyboardButton('Купить!', url='https://t.me/timur_py'))
