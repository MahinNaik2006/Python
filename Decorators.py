# what are decorators : way to modify functions or methods without altering their source code directly


def decorator(func):
    def wrapper(*args,**kwargs):
        func(*args,**kwargs)
        print('Decorator is called')

    return wrapper

@decorator
def hello(name):
    print(f'Hello {name} , Call Decorator')


hello('Mahin')