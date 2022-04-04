from firebase import firebase
import telepot
import time
from telepot.loop import MessageLoop
from pprint import pprint
from datetime import datetime

bot = telepot.Bot('change_to_your_TG_bot_token')

url = 'change_to_your_RealTimeDB_link_'
fb = firebase.FirebaseApplication(url,None)







    
def handle(msg):
    ID = msg['chat']['id']
    CHAT = msg['chat']['title']
    TYPE = msg['chat']['type']
    FROM = msg['from']['first_name']
    USERNAME = msg['from']['username']
    TEXT = msg['text']
    MESSAGE_ID =msg['message_id']
    now = datetime.now()
    date_time = now.strftime('%d/%m/%y, %H:%M:%S')
    DATE = str(date_time)

    data = {
        'id' : ID,
        'title': CHAT,
        'type' : TYPE,
        'from' : FROM,
        'text' : TEXT,
        'message_id': MESSAGE_ID,
        'date' : DATE,
    }

    print(data)
    

    fb.post('/chat_record', data)
    print('success')
    

MessageLoop(bot, handle).run_as_thread()


print("I'm listening...")    





while 1:
    message = fb.get('/data_need_to_send', None)
    if message is not None:
        message_send = message['message'] 
        if message_send == '/delete':
            fb.delete('/chat_record', None)
            pass
        else:
           bot.sendMessage('change_to_your_chatID', 
           message_send, parse_mode=None, 
           disable_web_page_preview=None, 
           disable_notification=False, 
           reply_to_message_id=None, 
           reply_markup=None)
           print(message)
           fb.delete('/data_need_to_send',None)
           pass
    time.sleep(5)