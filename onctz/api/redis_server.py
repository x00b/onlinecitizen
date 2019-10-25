import redis

host = "localhost"
port = 6379
passwd = 'passwd'

redis.Redis(host=host, port=port, db=0)
