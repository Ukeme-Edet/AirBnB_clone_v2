#!/usr/bin/env bash
# Install nginx and create directories
sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/{releases/test,shared}
sudo echo "<h1>Test</h1>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '38i\\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx restart
exit 0
