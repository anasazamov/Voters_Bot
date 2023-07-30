from telegram import Update, InlineKeyboardButton,ReplyKeyboardMarkup,InlineKeyboardMarkup
from telegram.ext import CallbackContext
from .models import Voters, Candidates

def start(update: Update, context: CallbackContext):
    
    try:
        voter = Voters.objects.get(username = update.message.chat.username)
        if voter.first_start:
            voter.chat_id = update.message.chat_id
            voter.first_start = False
            btn = InlineKeyboardButton("Ha",callback_data="ha")
            reply_markup = InlineKeyboardMarkup([[btn]])
            voter.save()
            update.message.reply_html("Ovoz berishiga tayyormisiz",reply_markup=reply_markup)
            
        else:
            update.message.reply_html("Ovoz berishni boshlagansiz")
    except Voters.DoesNotExist:
        pass

def candidate_func(update: Update, context: CallbackContext):
    if not ":" in update.callback_query.data:
        try:
            voter = Voters.objects.get(chat_id = update.callback_query.message.chat_id)
        except Voters.DoesNotExist:
            return None
        condidate = Candidates.objects.filter(voter=voter)
        chat_id = update.callback_query.message.chat_id
        message_id = update.callback_query.message.message_id
        for i in condidate:
            btn1 = InlineKeyboardButton("Ha",callback_data=f'{i.pk}:yes')
            btn2 = InlineKeyboardButton("Yo'q",callback_data=f'{i.pk}:no')
            reply_markup = InlineKeyboardMarkup([[btn1,btn2]])
            context.bot.send_message(text=f"<b>Ismi:</b>{i.first_name}\n<b>Familyasi:</b>{i.last_name}\n<b>Lavozimi:</b>{i.position}\n<b>Kafedra:</b>{i.department}",reply_markup=reply_markup)
        context.bot.delete_message(chat_id=chat_id,message_id=message_id)
    else: 
        chat_id = update.callback_query.message.chat_id
        message_id = update.callback_query.message.message_id
        id = update.callback_query.data.split(":")
        condidate = Candidates.objects.get(id=id[0])
        if id[1]=="yes":
            condidate.yes+=1
        elif id[1]=="no":
            condidate.no+=1
            
        condidate.save()
        context.bot.edit_message_text(chat_id=chat_id,message_id=message_id,text="Ovozingiz qabul qilindi")
        
         
        
    
    