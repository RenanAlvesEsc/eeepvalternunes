sudo systemctl daemon-reload;
sudo systemctl restart gunicorn.socket gunicorn.service;

sudo nginx -t
sudo service nginx restart
sudo service nginx reload
