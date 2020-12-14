import time
def decorator(fn):
    def wrapper():
        print("Calling function fn")
        start = time.time()
        value = fn()
        end = time.time()
        print("Call has ended")
        print(f"Time: {end - start}")
        return value
    return wrapper
@decorator
def foo() -> int:
    time.sleep(3)
    return 42
if __name__ == "__main__":
    print(foo())