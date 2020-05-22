from rediscluster import RedisCluster

def isExists(lst, key, value):
    for i, dic in enumerate(lst):
        if dic[key] == value:
            return i
    return -1

def doSomething(msg_id, raw_data):
    print(msg_id)
    print(raw_data)


STARTUP_NODES = [
    {"host": "192.168.36.71", "port": "7001"}
]

stream = "teststream"
group_name = "group1"
consumer_name = "consumer1"

rc = RedisCluster(startup_nodes=STARTUP_NODES, decode_responses=True)
rc.xgroup_destroy(stream, group_name)
rc.close()
