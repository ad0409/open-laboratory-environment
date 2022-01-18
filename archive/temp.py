import functools
import time
import logging


logging.basicConfig(format='%(levelname)s - %(asctime)s - %(message)s', datefmt='%d-%m-%y %H:%M:%S',
                    level=logging.WARNING)


a = 5
b = 0

# noinspection PyBroadException
try:
    c = a / b
except Exception as e:
    logging.warning('Exception occurred', exc_info=True)


def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat
    return decorator_repeat


def do_twice(func):
    def wrapper_do_twice():
        func()
        func()
    return wrapper_do_twice


def move(func):
    """Process parameters of correlating axis"""

    @functools.wraps(func)
    def wrapper_move(*args, **kwargs):
        func(*args, **kwargs)
        # return value
        return wrapper_move


def move_axes(axis_name=None, mm_wanted=0, v_wanted=0):  # linear moving axes
    if axis_name == 'home':
        print(str.encode(f"G28\n"))
    elif axis_name == 'X home':
        print(str.encode(f"X G28\n"))
    elif axis_name == 'Y home':
        print(str.encode(f"Y G28\n"))
    elif axis_name == 'Z home':
        print(str.encode(f"Z G28\n"))
    else:
        print(str.encode(f"F{v_wanted} GO {axis_name}{mm_wanted}\n"))


# elif axis_name == 'X home':
    #     print(str.encode(f"X G28\n"))


@repeat(num_times=1)
def flush():  # flush input-line before reading out data
    print('flushInput()')
    time.sleep(0.5)


@repeat(num_times=2)
def flush2():  # flush input-line before reading out data
    print('flushOutput()')
    time.sleep(0.5)


# def read_sensor()

""" move_axes(axis_name, mm_wanted, v_wanted) """
move_axes('X home')
move_axes('Y home')
move_axes('Z home')
move_axes('Z', -150, 2500)
flush()
flush2()


# SNIPPETS
# @move
# def move_x(mm_wanted_x, v_wanted_x):  # linear moving X
#     print('Linear moving X=' + mm_wanted_x + '[mm] ' + 'with Feedrate=' + v_wanted_x + '[mm/min]')
#     str.encode('F' + str(v_wanted_x) + ' G0 X ' + str(mm_wanted_x) + '\n')
#
#
# def move_y(mm_wanted_y, v_wanted_y):  # linear moving Y
#     print('Linear moving Y=' + mm_wanted_y + '[mm] ' + 'with Feedrate=' + v_wanted_y + '[mm/min]')
#     str.encode('F' + str(v_wanted_y) + ' G0 X ' + str(mm_wanted_y) + '\n')
#
#
# def move_z(mm_wanted_z, v_wanted_z):  # linear moving Z
#     print('Linear moving Z=' + mm_wanted_z + '[mm] ' + 'with Feedrate=' + v_wanted_z + '[mm/min]')
#     str.encode('F' + str(v_wanted_z) + ' G0 Z ' + str(mm_wanted_z) + '\n')


# print(move_x('50', '2000'))
# print(move_y('150', '1500'))
# print(move_z('50', '1000'))

# SNIPPETS
# def timer(func):
#     """Print the runtime of the decorated function"""
#
#     @functools.wraps(func)
#     def wrapper_timer(*args, **kwargs):
#         start_time = time.perf_counter()  # 1
#         value = func(*args, **kwargs)
#         end_time = time.perf_counter()  # 2
#         run_time = end_time - start_time  # 3
#         print(f"Finished {func.__name__!r} in {run_time:.4f} seconds.")
#         return value
#     return wrapper_timer
#
#
# @timer
# def waste_some_time(num_times):
#     for _ in range(num_times):
#         sum([i ** 2 for i in range(10000)])
#
#
# @timer
# def waste_some_time_3(num_times):
#     for _ in range(num_times):
#         sum([i ** 3 for i in range(10000)])


# print(waste_some_time(1))
# print(waste_some_time_3(2))
