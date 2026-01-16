import asyncio
import time

async def fetch_data(t):
    print(f"Do something with {t}...")
    time.sleep(t)
    print(f"Done with {t}")
    return f"Result of {t}"


async def main():
    t1=asyncio.create_task(fetch_data(1))
    t2=asyncio.create_task(fetch_data(2))
    result1=await t1
    print("Finished task 1")
    result2=await t2
    print("Finished task 2")
    return [result1,result2]


start=time.time()
result=asyncio.run(main())
end=time.time()
print(f"{end-start:.2f} seconds")
print(result)