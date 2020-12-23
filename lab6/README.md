# ==Lab 6==

Implemented on `Python with cProfile`.

#### Код без оптимізації:
```import time
from lab6 import profile, count_time


@count_time
@profile
def first_func():
    for i in range(100):
        time.sleep(1)


@count_time
@profile
def second_func():
    for i in range(100):
        time.sleep(1)


@count_time
@profile
def third_func():
    for i in range(100):
        time.sleep(1)

```
**Час виконання: ~300 секунд.**
##### Результат:
```102 function calls in 100.244 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.003    0.003  100.244  100.244 /Users/volodaorlov/Programing/python/allocator/lab6/unoptimized.py:5(first_func)
      100  100.241    1.002  100.241    1.002 {built-in method time.sleep}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



100.24234223365784
         102 function calls in 100.265 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001  100.265  100.265 /Users/volodaorlov/Programing/python/allocator/lab6/unoptimized.py:12(second_func)
      100  100.264    1.003  100.264    1.003 {built-in method time.sleep}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



100.26214671134949
         102 function calls in 100.274 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001  100.274  100.274 /Users/volodaorlov/Programing/python/allocator/lab6/unoptimized.py:19(third_func)
      100  100.272    1.003  100.272    1.003 {built-in method time.sleep}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

100.27108669281006
```

#### Оптимізований код:
```from lab6 import profile, count_time


@count_time
@profile
def first_func():
    for i in range(100):
        pass


@count_time
@profile
def second_func():
    for i in range(100):
        pass


@count_time
@profile
def third_func():
    for i in range(100):
        pass
```
##### Результат трьох функцій:
```         2 function calls in 0.000 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 /Users/volodaorlov/Programing/python/allocator/lab6/optimized.py:4(first_func)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



0.00019979476928710938
         2 function calls in 0.000 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 /Users/volodaorlov/Programing/python/allocator/lab6/optimized.py:11(second_func)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



0.00011730194091796875
         2 function calls in 0.000 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 /Users/volodaorlov/Programing/python/allocator/lab6/optimized.py:18(third_func)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



0.00011968612670898438
```
