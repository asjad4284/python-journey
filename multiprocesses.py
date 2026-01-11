from multiprocessing import Process
import time

def brew_chai(name):
    print(f"{name} is brewing.")
    time.sleep(3)
    print(f"{name} has brewed.")


if __name__== "__main__":
    chai_makers=[
        Process(target=brew_chai,args=(f"Chai maker #{i+1}",))
        for i in range(3)
    ]

    for p in chai_makers:
        p.start()
        p.join()
    
    # for p in chai_makers:
    
    print("All chai served!")