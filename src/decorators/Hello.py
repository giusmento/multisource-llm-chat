def hello_decorator(func):
    def wrapper(*args, **kwargs):
        print("Hello!")
        return func(*args, **kwargs)
    return wrapper