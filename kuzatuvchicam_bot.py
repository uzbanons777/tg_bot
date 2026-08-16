from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import logging

# ==================== BU JOYNI O'ZGARTIRING ====================
BOT_TOKEN = "8392021656:AAGfNoHQuPuFZH1gHXGYnWSW37SmhnL-DRk"
WEBAPP_URL = "https://uzbanons777.github.io/kuzatuvchi_cam/"  # Deploy qilgandan keyin
CHANNEL_ID = "@buyurtmalar_cam"  # Kanal username
# ================================================================

logging.basicConfig(format='%(asctime)s - %(levelname)s', level=logging.INFO)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Ilovani ochish", web_app=WebAppInfo(url=WEBAPP_URL))],
        [InlineKeyboardButton("Foydalanish yo'riqnomasi", callback_data="guide")],
    ]
    await update.message.reply_html(
        f"<b>Kuzatuv Cam</b>ga xush kelibsiz!\n\n"
        f"Ilovani ochish uchun tugmani bosing:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "guide":
        await query.edit_message_text(
            "<b>Yo'riqnoma</b>\n\n"
            "1.Ilovani ochish tugmasini bosing\n"
            "2.Ism va telefon raqam kiriting\n"
            "3.Mahsulotlarni ko'ring\n"
            "4.Savatga qo'shing va buyurtma bering",
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Orqaga", callback_data="back")]])
        )
    elif query.data == "back":
        keyboard = [
            [InlineKeyboardButton("Ilovani ochish", web_app=WebAppInfo(url=WEBAPP_URL))],
            [InlineKeyboardButton("Foydalanish yo'riqnomasi", callback_data="guide")],
        ]
        await query.edit_message_text(
            "<b>Kuzatuv Cam</b>ga xush kelibsiz!\n\n馃摫 Ilovani ochish uchun tugmani bosing:",
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


if __name__ == "__main__":
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    print("Bot ishga tushdi...")
    app.run_polling()
