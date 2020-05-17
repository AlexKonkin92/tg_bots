import telegram
from yaml import load
with open('tg_bot_token.yaml', 'r') as f:
    config = load(f)
token = config['bot_token']
bot = telegram.Bot( token )
for last_update in bot.getUpdates():
    chat_id = last_update.message.chat.id
#bot.sendMessage(chat_id = chat_id, text = 'Привет, Царь!')
bot.send_document(chat_id=chat_id, document=open('texts_rating.TXT', 'rb'))



