import asyncio
import random
import datetime

LOOP = 3


async def tcp_echo_client(message, port, loop):
    """
    async tcp client
    Args:
        message: send strings
        port: send tcp request to 127.0.0.0:port
        loop: event loop
    """
    # Asyncio でコネクションをオープン
    # オープン中は別の処理にスイッチされ別の処理が実行可能
    print("open connection....")
    reader, writer = await asyncio.open_connection('127.0.0.1', port,
                                                        loop=loop)
    # サーバー側にデータ送信
    print('Send: %r' % message)
    writer.write(message.encode())
    # Asyncio でサーバー側からデータ受信
    # データ受信中は別の処理にスイッチされ別の処理が実行可能
    data = await reader.read(3072)
    print('Received: %r' % data.decode())

    # コネクションクローズ
    print('Close the socket')
    writer.close()


async def multiple_request(loop):
    """
    ポート番号 8888, 8889, 8890 にデータ送信する3つのタスクを
    イベントループに登録する

    Args:
        loop: event loop
    """
    tasks = []
    port = 8888
    for i in range(0, LOOP):
        message = 'Hello World! {0}'.format(random.randint(0, 100)) 
        tasks.append(tcp_echo_client(message, port, loop))
        port += 1
    done, pending = await asyncio.wait(tasks)

loop = asyncio.get_event_loop()
start = datetime.datetime.now()
# イベントループにより処理を開始する。
loop.run_until_complete(multiple_request(loop))
end = datetime.datetime.now()
loop.close()
print("execution time: {0}".format(end - start))
