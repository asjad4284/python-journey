from multiprocessing import Process
import time

def brew_chai():
    print("Chai started brewing...")
    count=0
    for _ in range(10000000):
        count+=1
    print("Chai finished brewing...")


if __name__ == "__main__":
    p1=Process(target=brew_chai)
    p2=Process(target=brew_chai)

    start=time.time()

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end=time.time()

    print(f"Finished brewing in {end-start:.2f} seconds.")

