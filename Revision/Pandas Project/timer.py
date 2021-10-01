from timeit import default_timer as time


def timer(func):
    def fn(*args, **kwargs):
        before = time()
        return_val = func(*args, **kwargs)
        after = time()
        time_ms = (after - before) * 1000

        return return_val, time_ms

    return fn
