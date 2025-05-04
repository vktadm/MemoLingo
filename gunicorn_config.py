# Server socket
bind = "0.0.0.0:8000"

# Worker processes
workers = 4
worker_class = "uvicorn.workers.UvicornWorker"

# # Security
# limit_request_line = 4096
# limit_request_fields = 100
# limit_request_field_size = 8190

# Debugging
reload = False  # Set to True only for development!
# spew = False  # Server-wide trace printing (extremely verbose)

# Server mechanics
# preload_app = True  # Load application before forking workers
# max_requests = 1000  # Restart workers after this many requests
# max_requests_jitter = 50  # Randomize max_requests to avoid all workers restarting at once

# Logging
# accesslog = "-"  # Log to stdout
# errorlog = "-"   # Log to stdout
# loglevel = "info"
# access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

# Process naming
proc_name = "memolingo"  # Change this to your application name

# SSL Configuration (uncomment and configure if using HTTPS)
# keyfile = "/path/to/your/ssl/key.pem"
# certfile = "/path/to/your/ssl/cert.pem"
# ssl_version = "TLSv1_2"
# ciphers = "TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_128_GCM_SHA256"
