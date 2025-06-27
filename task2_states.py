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
    
    print(f"Задача 1 завершена: {task1.done()}")
    print(f"Задача 2 завершена: {task2.done()}")
    
    tasks = [task1, task2]
    
    for completed_task in asyncio.as_completed(tasks):
        result = await completed_task
        print(result)
        
    print(f"Задача 1 завершена: {task1.done()}")
    print(f"Задача 2 завершена: {task2.done()}")

asyncio.run(main())
