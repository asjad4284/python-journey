import asyncio
import time

async def f_data(t):
    await asyncio.sleep(t)
    return f"Result of {t}"

async def main():
    # Create task manually
    t1=asyncio.create_task(f_data(1))
    t2=asyncio.create_task(f_data(2))
    result1=await t1
    result2=await t2
    print(f"Result of task 1 and 2 are: {[result1,result2]}")

    # Gather Coroutines
    coroutines=[f_data(i) for i in range(1,3)]
    results=await asyncio.gather(*coroutines,return_exceptions=True)
    print(f"Coroutine Results: {results}")



start=time.time()
result=asyncio.run(main())
end=time.time()
print(f"{end-start:.2f} seconds")
# print(result)