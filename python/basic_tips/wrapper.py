class A:

    def __init__(self):
        self.funcs = []

    def over(self, x):

        def wrapper(f):

            def wrapped(*args, **kwargs):
                print(args, kwargs)
                return f(*args, **kwargs)

            self.funcs.append(wrapper)
            return wrapped

        return wrapper
