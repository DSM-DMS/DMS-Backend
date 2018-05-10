git pull 
kill $(ps a | grep python | grep -v "S+" | awk '{print $1}')
sudo -E python3.4 server.py