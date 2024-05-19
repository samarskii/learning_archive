import time
import psutil
import os


# Measure runtime and memory usage
def measure_performance(n):
    start_time = time.time()
    
    process = psutil.Process(os.getpid())
    mem_before = process.memory_info().rss / 1024  # in KB
    
    result = Solution().isHappy(n)
    
    mem_after = process.memory_info().rss / 1024  # in KB
    end_time = time.time()
    
    runtime = end_time - start_time
    memory_used = mem_after - mem_before
    
    print(f"Input: {n}")
    print(f"Result: {result}")
    print(f"Runtime: {runtime:.6f} seconds")
    print(f"Memory usage: {memory_used:.6f} KB")
    print("-" * 30)

# Test the function with examples
measure_performance(19)
measure_performance(2)