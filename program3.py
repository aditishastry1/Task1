import time
from functools import lru_cache

def count_ways_recursive(n: int) -> int:
    
   
    if n == 0:
        return 1  
    if n < 0:
        return 0 

    
    return (count_ways_recursive(n - 1) + 
            count_ways_recursive(n - 2) + 
            count_ways_recursive(n - 3))



def count_ways_memo(n: int, memo: dict = None) -> int:
    
    if memo is None:
        memo = {}

    
    if n == 0:
        return 1
    if n < 0:
        return 0

  
    if n in memo:
        return memo[n]

   
    memo[n] = (count_ways_memo(n - 1, memo) + 
               count_ways_memo(n - 2, memo) + 
               count_ways_memo(n - 3, memo))

    return memo[n]



@lru_cache(maxsize=None)
def count_ways_lru(n: int) -> int:
    if n == 0:
        return 1
    if n < 0:
        return 0
    return count_ways_lru(n - 1) + count_ways_lru(n - 2) + count_ways_lru(n - 3)



if __name__ == "__main__":
    
    print("=== Verification (Input: n = 4) ===")
    print(f"count_ways_recursive(4) = {count_ways_recursive(4)}")  
    print(f"count_ways_memo(4)      = {count_ways_memo(4)}")       
    print(f"count_ways_lru(4)       = {count_ways_lru(4)}")        

    
    n = 30
    print(f"\n=== Performance Benchmark (Input: n = {n}) ===")

    
    start_time = time.perf_counter()
    ans_rec = count_ways_recursive(n)
    end_time = time.perf_counter()
    time_rec = end_time - start_time
    print(f"Plain Recursion Result : {ans_rec}")
    print(f"Plain Recursion Time   : {time_rec:.6f} seconds")

   
    start_time = time.perf_counter()
    ans_memo = count_ways_memo(n)
    end_time = time.perf_counter()
    time_memo = end_time - start_time
    print(f"Memoized Result        : {ans_memo}")
    print(f"Memoized Time          : {time_memo:.8f} seconds")

    if time_memo > 0:
        speedup = time_rec / time_memo
        print(f"\nMemoization is approximately {speedup:,.2f}x faster for n = {n}!")
