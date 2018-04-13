from mitmproxy import ctx
import json
import stomp
import json
from urllib.parse import parse_qs,urlparse

class QueueDataAddon:
    def __init__(self):
        conn = stomp.Connection()
        conn.start()
        conn.connect('admin', 'admin', wait=True)
        self.qconn=conn

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
            self.qconn.send(body=json.dumps(data), destination=ctx.options.queueName)

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