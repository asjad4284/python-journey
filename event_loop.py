import asyncio

async def fetch_data(t):
    print(f"Do something with {t}...")
    await asyncio.sleep(t)
    print(f"Done with {t}")
    return f"Result of {t}"


async def main():
    # create_task() makes tasks in the event loop with sequence
    task1=asyncio.create_task(fetch_data(1))
    task2=asyncio.create_task(fetch_data(2))
    # In event loop,tasks are served as fifo
    resultt2= await task2
    print("Task 2 fully completed.")
    resultt1=await task1
    print("Task 1 fully completed.")
    return [resultt1,resultt2]

result=asyncio.run(main())
print(result)
