from time import time

def performence(func):
    def wrapper(*args , **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f"Runningtime it took is{t2-t1} seconds")
        return result
    return wrapper