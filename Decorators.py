# what are decorators : way to modify functions or methods without altering their source code directly

def decorator(func):
    def wrapper(*args,**kwargs):
        func(*args,**kwargs)
        print('Decorator is called')

    return wrapper

@decorator
def hello(name):
    print(f'Hello {name} , Call Decorator')


# --------------------------------- A Very good Example ----------------------

def logged(function):
    def wrap(*args,**kwargs):
        value = function(*args,**kwargs)
        with open('addList.txt' , 'a+') as F:
            F.write(f'The result is = {value}')
        return value
    return wrap

@logged
def add(x,y):
    print(f'The addition is = {x+y}')
    return x + y

#we can use the decorator for other function also

@logged
def diff(x,y):
    print(f'The difference is = {x-y}')
    return x - y


#you can call any of them
#add(3,4)
diff(50,10)
