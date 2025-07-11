from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import os

TOKEN = os.getenv(7652768419:AAEtsIyMUYoXi_2uW00gf-2JqfB93kvpNO8)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome! Send your serial video with caption: serial.mp4")

async def handle_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    caption = update.message.caption
    if not caption:
        await update.message.reply_text("Please add a caption like 'serial.mp4' or 'vlog.mp4'")
        return

    file = await update.message.video.get_file()
    await file.download_to_drive(caption)
    await update.message.reply_text(f"{caption} received!")

    # Check if both files are uploaded
    if os.path.exists("serial.mp4") and os.path.exists("background.mp4"):
        await update.message.reply_text("Processing video... (Dummy response)")
        # Real processing will happen here in future
        await update.message.reply_video("serial.mp4", caption="Final video (demo)")

app = ApplicationBuilder().token(7652768419:AAEtsIyMUYoXi_2uW00gf-2JqfB93kvpNO8).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.VIDEO, handle_video))

app.run_polling()
