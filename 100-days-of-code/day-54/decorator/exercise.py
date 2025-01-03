import time
 
def speed_calc_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} run speed: {end_time - start_time}s")
        return result
    return wrapper
 
@speed_calc_decorator
def fast_function():
  for i in range(1000000):
    i * i
 
@speed_calc_decorator
def slow_function():
  for i in range(10000000):
    i * i
 
fast_function()
slow_function()

#-------ALTERNATIVE-------#
# import time

# def speed_calc_decorator(function):
#     start_time = time.time()
#     function()
#     end_time = time.time()
#     return end_time - start_time

# def fast_function():
#   for i in range(1000000):
#     i * i
        

# def slow_function():
#   for i in range(10000000):
#     i * i

# print(f"fast_function run speed: {speed_calc_decorator(fast_function)}")
# print(f"slow_function run speed: {speed_calc_decorator(slow_function)}")
