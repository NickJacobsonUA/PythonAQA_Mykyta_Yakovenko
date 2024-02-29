from functools import wraps

def log_function_name(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_function_name
def add(x, y):
    return x + y

@log_function_name
def multiply(x, y):
    return x * y

print(add(2, 3))
print(multiply(2, 4))