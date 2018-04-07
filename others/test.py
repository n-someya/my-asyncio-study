import asyncio
import requests
import random
import aiohttp
random.seed()

#aiohttp.request('GET', 'https://google.com')

# イベントループ内で実行可能な処理を定義
async def asynfunc(x):
    # 非同期で実行したい重い処理を await で呼び出す
    print('start {0} task'.format(x))
    # TODO await で待っている処理の中で例外が発生した場合は補足方法があるみたい
    response = await heavy_task(x)
    print('end {0} task'.format(x))
    return response

## 非同期で実行したい重い処理
async def heavy_task(x):
    y = 0
    delay = int(random.random() * 10)
    print('start heavy task {1} {0}s'.format(delay, x))
    await asyncio.sleep(0)
    for i in range(0, 10000 + delay * 100):
        y += 1
    asyncio.sleep(delay)
    print('end heavy task {1} {0}s'.format(delay, x))
    return 'Hello! {0} {1}'.format(y, delay)

# イベントループを取得
loop = asyncio.get_event_loop()
features_heavy_task = [ asyncio.ensure_future(asynfunc(x), loop=loop) for x in range(0, 100)]
loop.run_until_complete(asyncio.wait(features_heavy_task))
#loop.stop()


# requests.get('https://google.com')