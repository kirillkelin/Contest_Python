from functools import wraps


def takes(*types):
    def decorator(func):
        @wraps(func)
        def wrapper(*args):
            if len(args) >= len(types):
                for i in range(len(types)):
                    if type(args[i]) != types[i]:
                        raise TypeError
                return func(*args)
            if len(args) < len(types):
                for i in range(len(args)):
                    if type(args[i]) != types[i]:
                        raise TypeError
                return func(*args)

        return wrapper

    return decorator


@takes(int, str)
def f(a, b):
    print(a, b)


try:
    f(1, 'str')
except Exception as e:
    print(type(e).__name__)
