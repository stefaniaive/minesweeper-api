import redis

redis_mines_structure = redis.StrictRedis(password="p6a4d3fbcd9f87a8800078068f301365cb3d58499ed6a45d69828d9168a57ce04", host='ec2-3-222-121-40.compute-1.amazonaws.com', port=18119, db=0)
redis_view_structure = redis.StrictRedis(password="p6a4d3fbcd9f87a8800078068f301365cb3d58499ed6a45d69828d9168a57ce04",host='ec2-3-222-121-40.compute-1.amazonaws.com', port=18119, db=1)
