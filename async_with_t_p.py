import asyncio
import time
from concurrent.futures import ProcessPoolExecutor

def fetch_data(t):
    print(f"Do something with {t}...",flush=True)
    time.sleep(t)
    print(f"Done with {t}",flush=True)
    return f"Result of {t}"

async def main():
    #Run in separate threads
    t1=asyncio.create_task(asyncio.to_thread(fetch_data,1))
    t2=asyncio.create_task(asyncio.to_thread(fetch_data,2))
    result1=await t1
    print(f"Finished thread 1")
    result2=await t2
    print(f"Finished thread 2")


    #Run in separate Process
    loop=asyncio.get_running_loop()
    with ProcessPoolExecutor() as executor:
        t1=loop.run_in_executor(executor,fetch_data,1)
        t2=loop.run_in_executor(executor,fetch_data,2)

        result1=await t1
        print("Finished process 1")
        result2=await t2
        print("Finished process 2")
    
    return [result1,result2]


if __name__=="__main__":
    start=time.time()

    result=asyncio.run(main())
    end=time.time()
    print(result)
    print(f"{end-start:.2f}")