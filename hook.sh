git pull 
kill $(lsof -i :$1 | grep python | awk '{print $2}')
sudo -E $2