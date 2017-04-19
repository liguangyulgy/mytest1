import asyncio

async def hello2(a):
    print("another hello")
    return 'testssss'


async def hello():
    print("Hello world!")
    r = await hello2(1)
    print("Hello again!%s" % r)

loop = asyncio.get_event_loop()
loop.run_until_complete(hello())
loop.close()