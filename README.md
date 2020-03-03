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

    $ python3 -m venv ./venv  # in the claps directory
    $ pip3 install requests
    $ pip3 install flask
    $ pip3 install gunicorn
    
As ufw allows incoming connection from all nodes on subnet 192.168.1.X, no ufw updates are needed.
Configure gunicorn and have supervisor monitor.

    $ sudo ln -s /home/pi/app/claps/claps_gunicorn.conf /etc/supervisor/conf.d/claps_gunicorn.conf
    $ sudo supervisorctl reread
    claps_gunicorn: available
    $ sudo supervisorctl update
    claps_gunicorn: added process group
    $ sudo supervisorctl status
    claps_gunicorn                   RUNNING   pid 22233, uptime 0:00:09

