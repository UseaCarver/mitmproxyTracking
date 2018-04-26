import stomp
import json
from os import environ
import threading
import time
import pika
import ast

msg_list=[]

class QueueSuscriber:
    def __init__ (self, callback):
        user_name_env=environ.get('USER_NAME')
        password_env=environ.get('PASSWORD')
        queue_destination = environ.get('QUEUE_DESTINATION')
        user= user_name_env if user_name_env is not None else 'admin'
        password= password_env if password_env is not None else 'admin'
        destination=queue_destination if queue_destination is not None else '/queue/mitmtrack'
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()
        print('Listening..')
        method_frame, header_frame, body = channel.basic_get('mitmtrack')
        print (method_frame, header_frame, body)
        if method_frame:
            print (method_frame, header_frame, body)
            channel.basic_ack(method_frame.delivery_tag)
            msg_list.append(json.loads(body))
            while method_frame.message_count > 0:
                method_frame, header_frame, body = channel.basic_get('mitmtrack')
                if method_frame:
                    channel.basic_ack(method_frame.delivery_tag)
                    msg_list.append(json.loads(body))
        else:
            print ('No message returned')
        channel.close()
        connection.close()
        callback(msg_list)