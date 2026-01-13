import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

def check_item(item):
    print(f"Checking {item} in store...")
    time.sleep(3)
    return f"{item} found : 42"

async def main():
    loop=asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        result=await loop.run_in_executor(pool,check_item,"Mac")
        print(result)

asyncio.run(main())
