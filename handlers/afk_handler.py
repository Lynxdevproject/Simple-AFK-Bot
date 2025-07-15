from datetime import datetime
from telegram import Update
from telegram.ext import ContextTypes

# 🗂️ Cache AFK user
afk_cache = {}
AFK_TRIGGER = "brb"

# 🧠 Format durasi AFK
def durasi_afk(since):
    delta = datetime.utcnow() - since
    menit = int(delta.total_seconds() // 60)
    return f"{menit} menit"

# 🚨 /afk command
async def afk_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    reason = " ".join(context.args) or "Tidak diketahui"
    afk_cache[user.id] = {"reason": reason, "since": datetime.utcnow()}
    await update.message.reply_text(
        f"😴 {user.first_name} sekarang AFK!\n📝 Alasan : {reason}\n⏳ Durasi : 0 menit"
    )

# 🔍 Handler teks biasa
async def afk_checker(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    message = update.message.text.lower()

    # 💤 Trigger AFK via "brb"
    if AFK_TRIGGER in message:
        afk_cache[user.id] = {"reason": update.message.text, "since": datetime.utcnow()}
        await update.message.reply_text(
            f"😴 {user.first_name} sekarang AFK!\n📝 Alasan : {update.message.text}\n⏳ Durasi : 0 menit"
        )
        return

    # 👋 User balik dari AFK
    if user.id in afk_cache:
        data = afk_cache.pop(user.id)
        await update.message.reply_text(
            f"👋 {user.first_name} telah kembali dari AFK!\n📝 Alasan : {data['reason']}\n⏳ Durasi : {durasi_afk(data['since'])}"
        )
        return

    # 🎯 Mention atau reply ke user yang AFK
    target = (
        update.message.reply_to_message.from_user
        if update.message.reply_to_message else None
    )
    if target and target.id in afk_cache:
        data = afk_cache[target.id]
        await update.message.reply_text(
            f"🙅 {target.first_name} lagi AFK!\n📝 Alasan : {data['reason']}\n⏳ Durasi : {durasi_afk(data['since'])}"
      )
