# onctz

----

##### Setup

###### Python
```
$ virtualenv --python=/usr/bin/python3.7 env
$ source env/bin/activate
$ pip install -r onctz/requirements.txt
```

###### Services
**Download Redis-Server**: https://redis.io/


##### Execution
[API] Terminal 0:
```
$ source env/bin/activate
$ python onctz/main.py
```
[RedisServer] Terminal 1:
```
$ ./redis-stable/src/redis-server
```
[Rq job Queues] Terminal 2:
```
$ cd onctz/
$ rq worker
```

