import multiprocessing

bind = '0.0.0.0:5050'
workers = multiprocessing.cpu_count() * 2 + 1
timeout = 360
worker_connections = 1000
