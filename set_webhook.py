import telegram


bot = telegram.Bot("6174496827:AAHbyTOlcL0CLo9w9aYmzCdN-0wvde_D1GI")
bot.set_webhook("https://tatu.pythonanywhere.com/api/bot")
print(bot.get_webhook_info())
