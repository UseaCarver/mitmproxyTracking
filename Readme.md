About

- Addon for mitmproxy to track your request and save it in activemq. 
- Run a server which can read data from activemq and return it back.

Preresiquites:

- python
- pip
- rabbitmq (Install via brew for MAC OS)
- mitmproxy (https://docs.mitmproxy.org/stable/overview-installation/#advanced-installation) (Install using 'pip3 install mitmproxy' for MAC)


Steps to run:
- Install dependencies: pip install -r requirements.txt
- Setup the proxy for your WiFi: python proxy/setup_proxy.py
- Start rabbitmq server: rabbitmq-server
- Start mitmproxy with addon: mitmdump -s ./proxy/queue_url_data_addon.py  --set urlToLog=www.google.co.in (Replace www.google.co.in with your url)
- Start the server to listen to track the url and view: python server/server.py
- Remove the proxy for your WiFi: python proxy/remove_proxy.py




