rabbitmqctl stop 
kill -9 `cat save_pid.txt` 
if [ $? -eq 0 ]; then
    echo 'Stopping mitmdump..'
    rm -rf save_pid.txt
fi
curl --request POST --url http://127.0.0.1:5000/shutdown 