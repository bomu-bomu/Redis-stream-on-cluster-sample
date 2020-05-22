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


group = rc.xinfo_groups(stream)
if isExists(group, "name", group_name) == -1:
    sys.exit("Stream group not found")

## Check Pending Message
print("## Check and work with Pending Message")
pending_lists = rc.xpending_range(stream, group_name, '-', '+', 100, consumer_name)
for msg in pending_lists:
    data = rc.xrange(stream, msg['message_id'], msg['message_id'])
    msg_id  = data[0][0]
    raw_data = data[0][1]
    doSomething(msg_id, raw_data)
    rc.xack(stream, group_name, msg_id)
