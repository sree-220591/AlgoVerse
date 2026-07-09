'''Algorithm
The gcd of two numbers is always <= min(a,b).
1.let smaller = min(a,b)
2.Check all the numbers from smaller to 1:
   if it divides a and b, then smaller is the gcd.
3.End'''

import time

def gcd_brute_force(a,b):
    smaller = min(a,b)
    for i in range(smaller,0,-1):
        if a % i == 0 and b % i == 0:
            return i
        
start = time.time()
result = gcd_brute_force(48, 18)
end = time.time()

print("Input: \n48, 18")
print(f"Output: \n{result}")
print(f"Execution Time: {end - start} seconds")