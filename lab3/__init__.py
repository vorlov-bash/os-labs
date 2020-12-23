import matplotlib.pyplot as plt

ADD_JOB_INTERVAL = 0.02
MAX_THREADS = 25

from lab3.priority_threads import ThreadManager, cron_worker

th_manager = ThreadManager(MAX_THREADS,
                           cron_worker)
th_manager.start()
