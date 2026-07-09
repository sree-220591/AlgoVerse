'''Approach: If d divides m and n, the d divides m mod n.'''

import time

def gcd(m,n):
    (a,b) = (max(m,n), min(m,n))
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    
start = time.time()
result = gcd(48,18)
end = time.time()

print("Input: \n48,18")
print(f"Output: \n{result}")
print("Execution Time:", end - start, "seconds")