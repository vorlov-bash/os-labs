import time
import threading
import typing


class PThread(threading.Thread):
    def __init__(self, target, args):
        super(PThread, self).__init__(target=target, args=args)
        self.init_start = time.time()

    def run(self):
        e_time = time.time() - self.init_start
        super().run()
        return e_time


class PriorQueue:
    def __init__(self):
        self.queue: typing.List[typing.Tuple[PThread, int]] = []

    def put(self, item: threading.Thread, prior):
        self.queue.append((item, prior))
        self.queue = sorted(self.queue, key=lambda elem: elem[1])

    def pop(self):
        return self.queue.pop(0)[0]


def some_worker(sleep_time):
    lock = threading.Lock()
    lock.acquire(timeout=8)
    try:
        time.sleep(sleep_time)
    finally:
        lock.release()
