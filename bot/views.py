from django.shortcuts import render
from django.views import View
from django.http import HttpRequest, JsonResponse
from telegram import Bot,Update
from telegram.ext import Dispatcher,CommandHandler,CallbackQueryHandler
from .callback import *
from json import loads
import os


# Create your views here.
TOKEN = os.environ["TOKEN"]
BOT = Bot(TOKEN)

class BotView(View):
    
    def get(request: HttpRequest,id):
        
        return JsonResponse({"status":200})
    
    def post(request:HttpRequest):
        
        data = loads(request.body.decode())
        dispatcher = Dispatcher(BOT,None,0)
        update: Update = Update.de_json(data,BOT)
        
        dispatcher.add_handler(CommandHandler("start",start))
        dispatcher.add_handler(CallbackQueryHandler(candidate_func))
        
        dispatcher.process_update(update)
        
        return JsonResponse({"status": 201})