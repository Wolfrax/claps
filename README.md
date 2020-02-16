Claps
=====

Finds all blog pages in the Pelican output directory (set by "father_root", see claps.py) by traversing the directory
tree. Then calling "https://api.applause-button.com/get-multiple" with a json-list of the blog pages (care taken that
get-multiple does not allow more than 100 entries in the list at the same time). The returned value is parsed and
rendered through a template file.

Claps depends on requests, flask and gunicorn, installation below. ufw needs to be configured to open the port used
by gunicorn (see claps_gunicorn.conf). Supervisor is used to monitorn gunicorn.

Installation
------------

    $ mkvirtualenv --python=/usr/bin/python3 claps
    $ pip3 install requests
    $ pip3 install flask
    $ pip3 install gunicorn
    $ sudo ufw allow from 192.168.1.0/24 to any port 8098
    Rule added
    $ sudo ufw status
    Status: active
    
    To                         Action      From
    --                         ------      ----
    8094                       ALLOW       192.168.1.0/24            
    80                         ALLOW       192.168.1.0/24            
    443                        ALLOW       192.168.1.0/24            
    22                         ALLOW       192.168.1.0/24            
    8096                       ALLOW       192.168.1.0/24            
    Bonjour                    ALLOW       Anywhere                  
    8098                       ALLOW       192.168.1.0/24            
    Bonjour (v6)               ALLOW       Anywhere (v6)
    
Configure gunicorn and have supervisor monitor.

    $ sudo ln -s /home/pi/app/claps/claps_gunicorn.conf /etc/supervisor/conf.d/claps_gunicorn.conf
    $ sudo supervisorctl reread
    claps_gunicorn: available
    $ sudo supervisorctl update
    claps_gunicorn: added process group
    $ sudo supervisorctl status
    claps_gunicorn                   RUNNING   pid 22233, uptime 0:00:09
    clover_gunicorn                  RUNNING   pid 4338, uptime 40 days, 14:11:41
    info_gunicorn                    RUNNING   pid 3525, uptime 40 days, 15:40:15
