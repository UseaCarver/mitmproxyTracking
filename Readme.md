About

- Addon for mitmproxy to track your request for a given url and save it in rabbitmq. 
- Run a server which can read data from rabbitmq and return it back.
- This could be used in writing automation tests for request going out of your machine. Like for web analytics data, background api calls for mobile etc.

How it works:

1. All the url requests from your machine is sent to the mitmproxy. 
2. The addon helps in sending the request body/ query string of the request to rabbitmq, only for the url passed as 'urlToLog'.
![alt text](https://raw.githubusercontent.com/bsneha90/mitmproxyTracking/master/mitmproxyTracking.png)
3. The server helps us to view/filter the data from the queue.
![alt text](https://raw.githubusercontent.com/bsneha90/mitmproxyTracking/master/server.png)

Preresiquites:
- python
- pip
- rabbitmq (Install via brew for MAC OS)
- mitmproxy (https://docs.mitmproxy.org/stable/overview-installation/#advanced-installation) (Install using 'pip3 install mitmproxy' for MAC)
- Setup mitmproxy certitficates if required, as mentioned [a here](https://docs.mitmproxy.org/stable/concepts-certificates/)

To start:
1. run sh ./start_tracking.sh 
2. setup the proxy for the device/machine

To stop and clean everything:
- sh ./stop-tracking.sh

API:

- 127.0.0.1:5000/view - to view all the data captured
- 127.0.0.1:5000/view?key1=value1&key2=value2 - to view data matching key1-value1 or key2-value2
- 127.0.0.1:5000/view/matching?key1=value1&key2=value2 - to view data matching key1-value1 and key2-value2




