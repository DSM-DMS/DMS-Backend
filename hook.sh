git pull 
kill $(ps aux | grep sudo\ -E\ python3.4\ server.py | awk '{print $2}')
sudo -E python3.4 server.py