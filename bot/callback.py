from telegram import Update, InlineKeyboardButton,ReplyKeyboardMarkup
from telegram.ext import CallbackContext
from .models import Voters, Candidates

def start(update: Update, context: CallbackContext):
    
    try:
        voter = Voters.objects.get(username = update.message.chat.username)
        if voter.first_start:
            voter.chat_id = update.message.chat_id
            voter.first_start = False
            btn = InlineKeyboardButton("Ha")
            reply_markup = ReplyKeyboardMarkup([[btn]],resize_keyboard=True)
            update.message.reply_html("Ovoz berishiga tayyormisiz",reply_markup=reply_markup)
        else:
            update.message.reply_html("Ovoz berishni boshlagansiz")
    except Voters.DoesNotExist:
        pass

def candidate(update: Update, context: CallbackContext):
    if not ":" in update.callback_query.data:
        try:
            voter = Voters.objects.get(chat_id = update.message.chat_id)
        except Voters.DoesNotExist:
            return None
        condidate: Candidates = voter.candidates
        for i in condidate:
            btn1 = InlineKeyboardButton("Ha",callback_data=f'{i.pk}:yes')
            btn2 = InlineKeyboardButton("Yo'q",callback_data=f'{i.pk}:no')
            reply_markup = ReplyKeyboardMarkup([[btn1,btn2]])
            
            update.message.reply_html(f"<b>Ismi:<b>{i.first_name}<br><b>Familyasi:<b>{i.last_name}<br>")
        
         
        
    
    