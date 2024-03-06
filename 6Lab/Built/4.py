import time
import math
def root(number, milliseconds):
    time.sleep(milliseconds / 1000)
    
    result = math.sqrt(number)
    print(f"Square root of {number} after {milliseconds} milliseconds is {result}")
a=int(input())
milliseconds=int(input())
root(a,milliseconds)
