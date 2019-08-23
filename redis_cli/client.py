import redis

redis_mines_structure = redis.StrictRedis(host='localhost', port=6379, db=0)
redis_view_structure = redis.StrictRedis(host='localhost', port=6379, db=1)