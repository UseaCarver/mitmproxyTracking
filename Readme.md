About

- Addon for mitmproxy to track your request and save it in rabbitmq. 
- Run a server which can read data from rabbitmq and return it back.

Preresiquites:

- python
- pip
- rabbitmq (Install via brew for MAC OS)
- mitmproxy (https://docs.mitmproxy.org/stable/overview-installation/#advanced-installation) (Install using 'pip3 install mitmproxy' for MAC)
- For mobile : 1.Proxy request to your machine's IP. 2. Follow mitmproxy steps for android/ios setup.


Steps to run:
- Install dependencies: pip install -r requirements.txt
- Setup the proxy for your WiFi: python proxy/setup_proxy.py (If running in mac, else setup in mobile manually)
- Start rabbitmq server: rabbitmq-server
- Start mitmproxy with addon: mitmdump -s ./proxy/queue_url_data_addon.py  --set urlToLog=www.google.co.in (Replace www.google.co.in with your url)
- Start the server to listen to track the url and view: python server/server.py
- Remove the proxy for your WiFi: python proxy/remove_proxy.py (If running in mac, else setup in mobile manually)


API:

- 127.0.0.1:5000/view - to view all the data captured
- 127.0.0.1:5000/view?key1=value1&key2=value2 - to view data matching key1-value1 or key2-value2
- 127.0.0.1:5000/view/matching?key1=value1&key2=value2 - to view data matching key1-value1 and key2-value2




