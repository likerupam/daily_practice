import time
import tracemalloc
from functools import wraps

def measure_performance(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Start measuring time and memory
        start_time = time.perf_counter()
        tracemalloc.start()
        
        result = func(*args, **kwargs)
        
        # Stop measuring time and memory
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.perf_counter()
        
        # Calculate performance metrics
        execution_time = end_time - start_time
        memory_used = peak / 1024 # Convert to KB
        
        print(f"Function '{func.__name__}' executed in {execution_time:.6f} seconds")
        print(f"Peak memory usage: {memory_used:.6f} KB")
        
        return result
    return wrapper