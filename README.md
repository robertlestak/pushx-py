# pushx-py

`pushx-py` is a simple wrapper library for [pushx](https://github.com/robertlestak/pushx). `pushx-py` exports a single function, `pushx`, which accepts two arguments, `input`, and `args`. `input` is the preformatted input data, and `args` is an array containing `pushx` configuration arguments. 

You must have `pushx` installed in order to use `pushx-py`.

See `examples/example.py` for an example of using one codebase and dynamically pushing to multiple services with a single configuration array.

Here is a basic example:

```python
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
```

Since the entire data layer configuration is contained within the `args` string slice, this can be moved to a configuration layer such as Vault or Consul. If you ever need to change the data layer configuration, you can simply update the `args` configuration, and your code will remain entirely the same.
