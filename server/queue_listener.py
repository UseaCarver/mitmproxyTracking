import json
import ast
import threading
import some_global

class ActiveQListener(object):
    print('ActiveQListener enter init')
    def __init__(self,callback):
        print('ActiveQListener init')
        self.msg_list = []
        self.callback=callback

    def on_error(self, headers, message):
        print('error occured')
        error={'error':message}
        self.msg_list.append(json.loads(error))

    def on_message(self, headers, message):
        print('Got message "%s"'% message)
        self.msg_list.append(ast.literal_eval(message))
        some_global.url_data_msg_list.append(ast.literal_eval(message))
        print('Sent message "%s"'% self.msg_list)
        print('Thread"%s"',threading.current_thread())
        self.callback(self.msg_list)

    def get_messages(self):
        print ('get_messages dump "%s"'%json.dumps(some_global.url_data_msg_list))
        print('Thread get_messages"%s"',threading.current_thread())
        return self.msg_list