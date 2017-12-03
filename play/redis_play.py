import redis

r = redis.Redis(host='localhost', port=6379, db=0)

r.zadd('ip_addresses', 'one', 1)
r.zadd('ip_addresses', 'three', 3)

r.zadd('ip_addresses', 'two', 2)

print(r.zrevrange('ip_addresses', 0, -1))