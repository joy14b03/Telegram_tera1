import telebot
import requests
from pyterabox import Terabox

# Replace with your bot token and Terabox credentials
bot = telebot.TeleBot('7237900259:AAGI2Wj4exxSSdzgYw2ZLgpYtT3SOBN_QJ0')
terabox = Terabox('b13titan.01@gmail.com', 'Laxmijb12')

@bot.message_handler(commands=['download'])
def download_terabox_video(message):
    # Get the Terabox video URL from the user
    video_url = message.text.split()[1]

    # Download the video using Terabox API
    video_path = terabox.download_file(video_url)

    # Upload the video to Telegram
    with open(video_path, 'rb') as video:
        bot.send_video(chat_id=message.chat.id, video=video)

bot.polling()
