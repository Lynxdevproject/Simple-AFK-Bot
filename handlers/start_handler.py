from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("➕ Tambahkan ke Grup", url="https://t.me/YOUR_BOT_USERNAME?startgroup=true")]
    ]
    await update.message.reply_text(
        "😴 *AFK Bot Simpel*\n\n"
        "Bot ini akan menandai kamu sebagai AFK jika kamu mengetik `/afk <alasan>` atau pesan mengandung kata `brb`. "
        "Kalau ada yang mention atau reply ke kamu, bot akan kasih tahu status AFK kamu.\n"
        "Begitu kamu kirim pesan lagi, bot akan nyambut kamu balik!\n\n"
        "➕ Tambahkan bot ini ke grup kamu untuk mulai mantau AFK.",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )
