from lab6 import profile, count_time


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
