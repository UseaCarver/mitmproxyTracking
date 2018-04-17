from mitmproxy import ctx
import json
import stomp
import json
from urllib.parse import parse_qs,urlparse
import pika


class QueueDataAddon:
    def __init__(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()
        self.channel=channel
        self.channel.queue_declare(queue='mitmtrack')

    def request(self, flow):
        if flow.request.host == ctx.options.trackUrl:
            if flow.request.method=='GET':
                url_query=urlparse(flow.request.url).query
                query_dict= {} if len(url_query)==0 else dict(item.split("=") for item in url_query.split("&"))
                print(query_dict)
                data = {'path':flow.request.url, 'data':query_dict }
            else:
                data = {'path':flow.request.url, 'data  ':json.loads(flow.request.text) }
            print('send data to queue')
            print(type(json.dumps(data)))
            self.channel.basic_publish(exchange='', routing_key='mitmtrack',body=json.dumps(data))

    def load(self, loader):
        loader.add_option(
            name = "trackUrl",
            typespec = str,
            default = "et2-m-virgintrains.ttlnonprod.com",
            help = "Url to track",
        )
        loader.add_option(
            name = "queueName",
            typespec = str,
            default = "/queue/mitmtrack",
            help = "Queue name",
        )
addons = [QueueDataAddon()]