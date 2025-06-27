import asyncio

async def worker(semaphore, number):
    async with semaphore:
        print(f"Работник {number} начал работу")
        await asyncio.sleep(2)
        print(f"Работник {number} завершил работу")

async def main():
    semaphore = asyncio.Semaphore(2)
    tasks = [worker(semaphore, i) for i in range(5)]
    await asyncio.gather(*tasks)

asyncio.run(main())
