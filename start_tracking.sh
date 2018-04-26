nohup
rabbitmq-server -detached
rabbitmqctl status > /dev/null
if [ $? -eq 0 ]; then
   sleep 2s
   pip3 list | grep -F mitmproxy
   if [ $? -eq 1 ]; then 
        echo 'installing mitmproxy'
        pip3 install mitmproxy
        echo 'please install the required certificates for https support'
   fi
   mitmdump -s ./proxy/queue_url_data_addon.py --set urlToLog=$1 >/dev/null & sleep 1s
   echo $! > save_pid.txt
   python3 ./server/server.py >/dev/null & sleep 1s
   echo $! > save_server_pid.txt
   echo 'Done'
fi
