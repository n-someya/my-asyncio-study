"""
$ python tcp_echo_sleep_server.py {port_number}

Ex:
$ python tcp_echo_sleep_server.py 8888

So, start server on port 8888.
And reply tcp echo message after 1s.
"""
import asyncio
import time
import sys

@asyncio.coroutine
def handle_echo(reader, writer):
    data = yield from reader.read(3072)
    message = data.decode()
    addr = writer.get_extra_info('peername')
    print("Received %r from %r" % (message, addr))

    time.sleep(1)

    print("Send: %r" % message)
    writer.write(data)
    yield from writer.drain()

    print("Close the client socket")
    writer.close()

loop = asyncio.get_event_loop()
coro = asyncio.start_server(handle_echo, '127.0.0.1', sys.argv[1], loop=loop)
server = loop.run_until_complete(coro)

# Serve requests until Ctrl+C is pressed
print('Serving on {}'.format(server.sockets[0].getsockname()))
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

# Close the server
server.close()
loop.run_until_complete(server.wait_closed())
loop.close()