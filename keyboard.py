from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

def main_keyboard():
    keyboard = [
        [KeyboardButton('/start'), KeyboardButton('/schedule'), KeyboardButton('/donate')]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

def inline_keyboard():
    keyboard = [
        [InlineKeyboardButton('Перейти на сайт', callback_data='visit_site')],
        [InlineKeyboardButton('Написать сообщение', callback_data='send_message')],
        [InlineKeyboardButton('Полезные ресурсы', callback_data='useful_resources')],
        [InlineKeyboardButton('Регистрация на ближайшие мероприятия', callback_data='event_registration')]
    ]
    return InlineKeyboardMarkup(keyboard)
