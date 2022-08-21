import json
from src.pushx import pushx

data = {
    'name': 'John Doe',
    'age': '42',
    'work': 'programmer',
}

args = [
    "-driver",
    "redis-list",
    "-redis-host",
    "localhost",
    "-redis-port",
    "6379",
    "-redis-key",
    "test-redis-list",
]

input = json.dumps(data)
pushx.pushx(input, args)