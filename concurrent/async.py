import asyncio
import time


def sleep():
    print(f'Time: {time.time() - start:.5f}')
    time.sleep(1)


def sum(name, numbers):
    total = 0
    for number in numbers:
        print(f'Task {name}: Computing {total}+{number}')
        sleep()
        total += number
    print(f'Task {name}: Sum = {total}\n')


def exe():
    tasks = [
        sum("A", [1, 2]),
        sum("B", [1, 2, 3]),
    ]

    end = time.time()
    print(f'Time: {end-start:.5f} sec; \n\n')


# Then the asyncio version
async def async_sleep():
    print(f'Time: {time.time() - start:.9f}')
    await asyncio.sleep(1)


async def async_sum(name, numbers):
    total = 0
    for number in numbers:
        print(f'Task {name}: Computing {total}+{number}')
        await async_sleep()
        total += number

    print(f'Task {name}: Sum = {total}\n')


def async_exe():
    """
    async version
    """
    loop = asyncio.get_event_loop()
    tasks = [
        loop.create_task(async_sum("A", [1, 2])),
        loop.create_task(async_sum("B", [1, 2, 3])),
    ]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

    end = time.time()
    print(f'Time: {end-start:.9f} sec;')


start = time.time()

async_exe()
