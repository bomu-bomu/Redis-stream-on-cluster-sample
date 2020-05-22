from rediscluster import RedisCluster
import time

STARTUP_NODES = [
    {"host": "192.168.36.71", "port": "7001"}
]

stream = "teststream"
rc = RedisCluster(startup_nodes=STARTUP_NODES, decode_responses=True)
while True:
    rc.xadd(stream, {"name": "sample1"})
    time.sleep(1)
rc.close()
