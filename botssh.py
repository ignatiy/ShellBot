from tokens import *

from datetime import datetime
from subprocess import Popen, PIPE, STDOUT
import operator
import collections

import time

import telepot



poll = 300  # seconds
shellexecution = []
setpolling = []
stopmarkup = {'keyboard': [['Stop']]}
hide_keyboard = {'hide_keyboard': True}

def clearall(chat_id):
    if chat_id in shellexecution:
        shellexecution.remove(chat_id)



class RPI3Bot(telepot.Bot):
    def __init__(self, *args, **kwargs):
        super(RPI3Bot, self).__init__(*args, **kwargs)
        self._answerer = telepot.helper.Answerer(self)
        self._message_with_inline_keyboard = None

    def on_chat_message(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)

        print("Your chat_id:" + str(chat_id)) 
        if chat_id in adminchatid:  # Store adminchatid variable in tokens.py
            if content_type == 'text':
                if msg['text'] == '/start' and chat_id not in shellexecution:
                    bot.sendMessage(chat_id, "Здравствуйте! для того чтобы начать работать, отправьте команду /shell" )
                   

                    now = datetime.now()

                    bot.sendMessage(chat_id, reply, disable_web_page_preview=True)
                elif msg['text'] == "Stop":
                    clearall(chat_id)
                    bot.sendMessage(chat_id, "Все операции остановлены.", reply_markup=hide_keyboard)

                elif msg['text'] == "/shell" and chat_id not in shellexecution:
                    bot.sendMessage(chat_id, "Отлично, теперь вы можете выполнить команду в терминале.",  reply_markup=stopmarkup)
                    shellexecution.append(chat_id)
                     
                elif chat_id in shellexecution:
                    bot.sendChatAction(chat_id, 'typing')
                    p = Popen(msg['text'], shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
                    output = p.stdout.read()
                    if output != b'':
                        bot.sendMessage(chat_id, output, disable_web_page_preview=True)
                    else:
                        bot.sendMessage(chat_id, "Возникла внутренняя ошибка.. НО(!!!), возможно команда выполнена. Проверьте!", disable_web_page_preview=True) 



TOKEN = telegrambot

bot = RPI3Bot(TOKEN)
bot.message_loop()
tr = 0
xx = 0
# Keep the program running.
while 1:
    if tr == poll:
        tr = 0
        timenow = datetime.now()
      
    time.sleep(10)  # 10 seconds
    tr += 10
