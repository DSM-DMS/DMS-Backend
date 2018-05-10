git pull 
kill $(ps a | grep python | egrep "S|Sl|Z|R" | awk '{print $1}')
sudo -E python3.4 server.py