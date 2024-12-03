import logging
# import requests
import time
from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    WebAppInfo,
    Update,
)
from telegram.ext import (
    Application,
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    ExtBot,
    MessageHandler,
    CallbackQueryHandler,
    filters,
)
from datetime import datetime
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

# Telegram bot token
TOKEN = os.getenv("BOT_TOKEN")


def setUserId(context: ContextTypes.DEFAULT_TYPE):
    # Init the user
    # response = requests.post(
    #     f"{SERVER}/api/v1/user", json={"user_id": context.chat_data["userId"]}
    # )

    # referralUser = InlineKeyboardButton(
    #     text="🪄 Invite the User", callback_data="inviteBtn"
    # )
    # registration = InlineKeyboardButton(
    #     text="📲 REGISTRATION",
    #     url="https://thlbots.com/?type=registration&lead_id=1226492"
    # )
    # checkRegistration = InlineKeyboardButton(
    #     text="🔍 CHECK REGISTRATION", callback_data="checkRegistration"
    # )
    play = InlineKeyboardButton(
        text="PLAY 💰", web_app=WebAppInfo(
            # "https://t.me/TestMyFirstTGBestBot/flash_lottery"
            "https://mini-app-frontend-pink.vercel.app/"
        ),
    )
    # messageMe = InlineKeyboardButton(
    #     text="👨🏾‍💻 Message me",
    #     url="https://t.me/Mark_VIP_AI_bot"
    # )

    configKeyboardMarkup = InlineKeyboardMarkup(
        [
            # [registration],
            [play],
            # [messageMe],
            # [userProfile],
        ]
    )


    return configKeyboardMarkup

async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the button click."""
    query = update.callback_query
    await query.answer() # Acknowledge the button click

    callback_data = query.data
    video_caption = """
Deposits have been credited✅
😇Congratulations, now you can join the private channel and get access to signals from our SOFTWARE!

If you have any questions, click the "message me" button.
"""
    video_file = open("./vip.mp4", "rb")

    if callback_data == "checkRegistration":
        await context.bot.send_video(
            chat_id=update.effective_chat.id,
            video=video_file,
            caption=video_caption,
            reply_markup=afterDepositMarkup,)

# start commmand
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("started!!!")
    # Get User ID
    context.chat_data["userId"] = update.effective_message.chat_id
    # Set User
    configKeyboardMarkup = setUserId(context)
    # photo_file = open("./back.jpg", "rb")

    # Hello Message
    descText = f"""
    Hi
    """
    # certification = f"\n<b>Made with ❤️ by Bitcoin Millionaire Team</b>"

    # Send the image with the text
    # await context.bot.send_photo(
    #     chat_id=update.effective_chat.id,
    #     photo=photo_file,
    #     caption=descText,
    #     reply_markup=configKeyboardMarkup,
    # )
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=descText,
        reply_markup=configKeyboardMarkup,
    )


if __name__ == "__main__":
    application = Application.builder().token(TOKEN).build()

    # Add handler to the bot
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_click))
    # application.add_handler(
    #     MessageHandler(filters.Text and ~filters.COMMAND, handleMessage)
    # )

    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    application.run_polling(allowed_updates=Update.ALL_TYPES)
