'''Algorithm:
Suppose d divides m and n, then m = ad and n = bd for some integers a and b. Then m - n = ad - bd = (a - b)d, so d divides m - n. Therefore, the gcd of two numbers does not change if the larger number is replaced by its difference with the smaller number.
So in conclusion, if d divides m and n, then d divides m - n.
1.If a % b == 0, then gcd(a,b) = b
2.otherwise gcd(a,b) = gcd(b, a - b).'''

import time

def gcd(m,n):
    (a,b) = (max(m,n), min(m,n))
    if a % b == 0:
        return b
    else:
        return gcd(b,a-b)
    
start = time.time()
result = gcd(48,18)
end = time.time()

print("Input: \n48,18")
print(f"Output: \n{result}")
print("Execution Time:", end - start, "seconds")