import asyncio
import time

async def brew_chai():
    start=time.time()
    print("Brew chai...")
    await asyncio.sleep(2)
    print("Chai is ready.")
    end=time.time()
    print(f"{end-start} seconds")
    


asyncio.run(brew_chai())
