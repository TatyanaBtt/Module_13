import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    num_bools = range(1,6)
    for num in num_bools:
        await asyncio.sleep(1/power)
        print(f'Силач {name} поднял {num} шар.')
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Fedya', 3))
    task2 = asyncio.create_task(start_strongman('Kolya', 4))
    task3 = asyncio.create_task(start_strongman('Alex', 5))
    await task1
    await task2
    await task3

asyncio.run(start_tournament())

