import telegram
import os 

TOKEN = os.environ["TOKEN"]

bot = telegram.Bot(TOKEN)
print(bot.set_webhook("https://tatu.pythonanywhere.com/api/bot/v2"))
# print(bot.delete_webhook())
print(bot.get_webhook_info())
