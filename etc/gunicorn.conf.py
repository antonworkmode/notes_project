# vi etc/gunicorn.conf.py

import multiprocessing

bind = 'unix:/run/gunicorn.sock'
workers = multiprocessing.cpu_count() * 2 + 1

accesslog = '/home/django/logs/notes_project/gunicorn-access.log'
errorlog = '/home/django/logs/notes_project/gunicorn-error.log'
loglevel = 'debug'
capture_output = True
