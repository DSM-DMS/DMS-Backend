git pull 
PID=$!
echo PID
kill -INT $PID
sudo -E python3.4 server.py