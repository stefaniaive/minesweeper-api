import redis
# REDIS_URL: redis://h:p37b50b38b08e9c1972c671e325b9b4b73834301c7ef309bb009937e117cacd29@ec2-34-227-251-50.compute-1.amazonaws.com:17169

redis_mines_structure = redis.StrictRedis(password="p37b50b38b08e9c1972c671e325b9b4b73834301c7ef309bb009937e117cacd29", host='ec2-34-227-251-50.compute-1.amazonaws.com', port=17169, db=0)
redis_view_structure = redis.StrictRedis(password="p37b50b38b08e9c1972c671e325b9b4b73834301c7ef309bb009937e117cacd29",host='ec2-34-227-251-50.compute-1.amazonaws.com', port=17169, db=1)
