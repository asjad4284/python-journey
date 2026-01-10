from multiprocessing import Process
import time

def brew_chai(name):
    print(f"{name} is brewing.")
    time.sleep(3)
    print(f"{name} has brewed.")


