import asyncio

async def api_call_1():
    await asyncio.sleep(2)
    return "Результат API 1"

async def api_call_2():
    await asyncio.sleep(1)
    return "Результат API 2"

async def main():
    task1 = asyncio.create_task(api_call_1())
    task2 = asyncio.create_task(api_call_2())
    
    result1 = await task1
    result2 = await task2
    
    print(result1)
    print(result2)

asyncio.run(main())
