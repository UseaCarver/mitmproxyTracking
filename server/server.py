from flask import Flask,request
import json
import time
import ast
from queue_subscribe import QueueSuscriber
from helper import Helper
app = Flask(__name__)
queueSuscriber = QueueSuscriber()

@app.route('/view')
def view():
    filters=request.args
    messages=queueSuscriber.get_messages()
    print(messages)
    print(type(messages))
    if len(request.args.items()) ==0 :
        return json.dumps(messages)
    else:
        helper = Helper()
        print(type(filters.iteritems()))
        return json.dumps(helper.filter_items(messages,filters.iteritems()))

@app.route('/view/matching')
def view_matching():
    filters=request.args
    messages=queueSuscriber.get_messages()
    if len(request.args.items()) ==0 or messages is None:
        return json.dumps(messages)
    else:
        helper = Helper()
        print(type(filters.iteritems()))
        return json.dumps(helper.filter_items_if_all_filters_match(messages,filters.iteritems()))

if __name__ == "__main__":
    app.run(debug=True)





