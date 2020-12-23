import threading
import time
import random
import statistics
import sys
from lab3.utils import PriorQueue, PThread, some_worker
from lab3 import MAX_THREADS, ADD_JOB_INTERVAL

wait_array = []


class ThreadManager:
    def __init__(self, max_threads: int, cron_target):
        self.q = PriorQueue()
        self.max_threads: int = max_threads
        self.cron_thread = threading.Thread(target=cron_target, args=(self, MAX_THREADS,))

    def add_thread(self):
        if len(self.q.queue) < self.max_threads:
            worker_time = random.uniform(0.001, 0.032)
            t = PThread(target=some_worker, args=(worker_time,))
            # print(f'WORKER \t>> {t.name} \tinited.\tTime:\t{t.init_start}.\tExecution time:\t{worker_time}')
            self.q.put(t, random.randint(1, 16))

    def start(self):
        self.cron_thread.start()
        self.cron_thread.join()
        while True:
            if self.q.queue:
                print(f'\033[96mMANAGER \t>> Queue size: {len(self.q.queue)}\033[0m')
                t = self.q.pop()
                init_time = time.time() - t.init_start
                wait_array.append(init_time)
                print(
                    f'\033[93mRUN \t>> {t.name} \tprepare to run. Total init time: {init_time}\033[0m')
                t.run()
            elif not self.cron_thread.is_alive():
                break
        print(f'\033[92m\nAVERAGE INIT: {statistics.mean(wait_array)}')

    def stop(self):
        sys.exit(1)


def cron_worker(t: ThreadManager, size: int):
    lock = threading.Lock()
    for i in range(size):
        lock.acquire()
        try:
            t.add_thread()
            # print(f'\033[96mMANAGER \t>> Queue size: {len(t.q.queue)}\033[0m\n')
            time.sleep(ADD_JOB_INTERVAL)
        finally:
            lock.release()


