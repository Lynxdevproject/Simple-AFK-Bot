import os
from dotenv import load_dotenv
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

# 🔧 Import handler modular
from handlers import start, afk_command, afk_checker

# 🔐 Load token dari .env
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# 🛠️ Error handler
async def error_handler(update, context):
    print(f"[ERROR] {context.error}")

# 🚀 Entry point bot AFK
def main():
    if not BOT_TOKEN:
        print("❌ BOT_TOKEN tidak ditemukan. Pastikan sudah diatur di .env")
        return

    app = Application.builder().token(BOT_TOKEN).build()

    # 🔍 Ambil info bot (username, dll)
    async def setup():
        bot_info = await app.bot.get_me()
        bot_username = bot_info.username
        app.bot_data["username"] = bot_username
        print(f"✅ Bot aktif sebagai @{bot_username}")

    # 📌 Handler /start + tombol invite
    app.add_handler(CommandHandler("start", start))

    # 📌 Handler /afk command
    app.add_handler(CommandHandler("afk", afk_command))

    # 📌 Handler teks biasa → deteksi brb, mention, comeback
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, afk_checker))

    # 📌 Error handler
    app.add_error_handler(error_handler)

    # 🧠 Jalankan setup sebelum polling
    app.post_init = setup

    print("😴 AFK Bot siap mantau tongkrongan...")
    app.run_polling()

if __name__ == "__main__":
    main()
