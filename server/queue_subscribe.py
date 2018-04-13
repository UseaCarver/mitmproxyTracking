import stomp
import json
from queue_listener import ActiveQListener 
from os import environ
import threading
import time

msg_list=[]

def update_message(msgs):
    print('updating')
    print(msgs)
    global msg_list
    msg_list=msgs
        
class QueueSuscriber:
  

    def __init__ (self):
        user_name_env=environ.get('USER_NAME')
        password_env=environ.get('PASSWORD')
        queue_destination = environ.get('QUEUE_DESTINATION')
        user= user_name_env if user_name_env is not None else 'admin'
        password= password_env if password_env is not None else 'admin'
        destination=queue_destination if queue_destination is not None else '/queue/mitmtrack'

        self.conn = stomp.Connection()
        print('intialize queue suscriber')
        self.msg_list=[{'a':'123'}]
        self.listner = ActiveQListener(update_message)
        self.conn.set_listener('',self.listner)
        self.conn.start()
        self.conn.connect(user,password, wait=True)
        self.conn.subscribe(destination=destination, id=1, ack='auto')
    
   
    
    def get_messages(self):
       msg= self.listner.get_messages()
       print('get_messages 1 "%s"'%self.listner.msg_list)
       print('get_messages "%s"'%msg_list)
       return msg