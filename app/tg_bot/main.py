from io import BytesIO
import requests
import telebot
from PIL import Image


token = "7941735220:AAEPCPeHsdpCTRjo0sLlqhY5MPubFjDmSZs"
bot = telebot.TeleBot(token)



@bot.message_handler(content_types=['photo'])
def handle_photos(message):
    file_id = message.photo[-1].file_id 
    file_info = bot.get_file(file_id) 
    downloaded_file = bot.download_file(file_info.file_path) 
    headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/91.0.4472.124 Safari/537.36 '
        }
    
    files = {'file': downloaded_file}
    response = requests.post("http://127.0.0.1:8000/uploadfile",headers=headers, files=files)

    if response.status_code == 200:
        img_bytes = response.content
        headers = response.headers
        size = headers.get("size", "0")
        bot.send_photo(message.chat.id, img_bytes)    
        bot.send_message(message.chat.id, f"Size is {size}")
    else:
        print(f"Error: {response.status_code}")

# Start the bot
if __name__ == "__main__":
    print("Bot is running...")
    bot.infinity_polling()