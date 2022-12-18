import multiprocessing

# Non logging stuff
bind = "0.0.0.0:8000"

# take advantage of full processor
workers = multiprocessing.cpu_count() * 2 + 1
# Access log - records incoming HTTP requests
accesslog = "/var/log/gunicorn.access.log"
# Error log - records Gunicorn server goings-on
# errorlog = "/var/log/gunicorn.error.log"
errorlog = "-"
# Whether to send Django output to the error log
capture_output = True
# How verbose the Gunicorn error logs should be
loglevel = "debug"
timeout = 72
