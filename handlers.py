from telegram import Update
from telegram.ext import ContextTypes
from keyboard import main_keyboard, inline_keyboard

async def schedule(update: Update, context: ContextTypes.DEFAULT_TYPE):
    schedule_message = (
        "Расписание ближайших мероприятий:\n\n"
        "1. Вебинар по фотографированию - 10 июля, 18:00\n"
        "2. Мастер-класс по рисованию - 15 июля, 14:00\n"
        "3. Онлайн встреча любителей книг - 20 июля, 19:00"
    )
    await update.message.reply_text(schedule_message)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        'Привет! Выберите команду:',
        reply_markup=main_keyboard()
    )
    await update.message.reply_text('Выберите действие:', reply_markup=inline_keyboard())

async def donate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    donate_message = (
        "Спасибо за ваше желание поддержать наш канал!\n"
        "Вы можете сделать пожертвование по следующим реквизитам:\n\n"
        "Сбербанк: 1234 5678 9012 3456\n"
        "Тинькофф: 9876 5432 1098 7654\n"
        "PayPal: example@example.com\n\n"
        "Все пожертвования пойдут на развитие нашего канала. Спасибо!"
    )
    await update.message.reply_text(donate_message)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'visit_site':
        await query.message.reply_text('Перейдите по ссылке: https://example.com')
    elif query.data == 'send_message':
        await query.message.reply_text('Напишите сообщение: @yourusername')
    elif query.data == 'useful_resources':
        await query.message.reply_text('Полезные ресурсы: https://useful-resources.com')
    elif query.data == 'event_registration':
        await query.message.reply_text('Для регистрации на ближайшие мероприятия, пожалуйста, заполните форму: https://registration-form.com')

async def inline_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Выберите действие:', reply_markup=inline_keyboard())
