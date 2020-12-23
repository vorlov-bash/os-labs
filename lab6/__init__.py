import cProfile
import io
import pstats
import time


def profile(func):
    def wrapper(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        ret_val = func(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        ps = pstats.Stats(pr, stream=s).sort_stats('cumulative')
        ps.print_stats()
        print(s.getvalue())
        return ret_val

    return wrapper


def count_time(f):
    def wrapper():
        t = time.time()
        f()
        print(time.time() - t)

    return wrapper()
