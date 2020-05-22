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

## If group not exists, create one
group = rc.xinfo_groups(stream)
if isExists(group, "name", group_name) == -1:
    rc.xgroup_create(stream, group_name, 0)

## Continue fetch data from stream
print("## Continue fetching data")
data = rc.xreadgroup(groupname = group_name,
                             consumername = "consumer1",
                             streams = { stream : '>'},
                             count = 10
                             ) 

result_stream_name = data[0][0]
messages = data[0][1]

for msg in messages:
    msg_id = msg[0]
    raw_data = msg[1]
    doSomething(msg_id, raw_data)
    rc.xack(stream, group_name, msg_id)

rc.close()
