from rediscluster import RedisCluster

def doSomething(msg_id, raw_data):
    print(msg_id)
    print(raw_data)


STARTUP_NODES = [
    {"host": "192.168.36.71", "port": "7001"}
]

stream = "teststream"

rc = RedisCluster(startup_nodes=STARTUP_NODES, decode_responses=True)

## Continue fetch data from stream
print("## Continue fetching data")
data = rc.xread( streams = { stream : '0'})

result_stream_name = data[0][0]
messages = data[0][1]

for msg in messages:
    msg_id = msg[0]
    raw_data = msg[1]
    doSomething(msg_id, raw_data)

rc.close()
