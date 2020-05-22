# Example code for using redis-stream in Redis Cluster via redis-py-cluster

## requirement
- python3
- redis
- redis-py-cluster

## File list

1. stream-producer.py -  feed stream with xadd
2. stream-xread.py - read stream with xread
3. stream-xreadgroup.py - demonstate xreadgroup and xack from stream
4. stream-xpending - Reexecute pending message (Pending message is the messages that retrieved from xreadgroup but not xack)




