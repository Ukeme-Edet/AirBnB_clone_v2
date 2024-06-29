#!/usr/bin/env bash
# Install nginx and create directories
sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/{releases/test,shared}
sudo echo "<h1>Test</h1>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo echo "server {
	listen 80;
	listen [::]:80 default_server;

	root /var/www/html;
	index index.html index.htm index.nginx-debian.html;

	server_name _;

	location /redirect_me {
		return 301 https://youtu.be/dQw4w9WgXcQ?si=c5SSrhdJz17xP0kV;
	}

	error_page 404 /404.html;
	location = /404.html {
		root /var/www/html;
		internal;
	}

	location /hbnb_static {
		alias /data/web_static/current;
	}
}" | sudo tee /etc/nginx/sites-available/default
sudo service nginx restart
exit 0
