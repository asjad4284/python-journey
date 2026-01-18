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


result=asyncio.run(main())
# print(result)