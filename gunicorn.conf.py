import multiprocessing

# host = '127.0.0.1'
# port = '8500'
# bind = host + ':' + port
workers = 4         # recommended: multiprocessing.cpu_count() * 2 + 1
worker_class = 'sync'
# pidfile = 'logs/pid_file.txt'
loglevel = 'debug'
accesslog = '-'     # accesslog = 'logs/access.log'
errorlog  = '-'     # errorlog = 'logs/error.log'
