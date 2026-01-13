import asyncio
import time

async def brew(name):
    print(f"Brewing {name}")
    await asyncio.sleep(3)
    # time.sleep(3)
    print(f"{name} is ready.")

async def main():
    start=time.time()
    await asyncio.gather(
        brew("Masala chai"),
        brew("Green chai")
    )
    end=time.time()
    print(f"{end-start} seconds.")

asyncio.run(main())