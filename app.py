import numpy as np
import math
import random
import os;

print('Increasing on interval function integrator:')

#define desired function to integrate (must be increasing on desired interval)
def function(x):
    return math.exp(x)
    
print('n(accuracy):')
n = input()    
print("Upper Bound:")
x_ulim = input()
x_ulim = float(x_ulim)
print('Lower Bound:')
x_blim = input()
x_blim = float(x_blim)


count = 0.0
in_area = 0.0

#plots n dots
while count < int(n):
    x_coord = random.uniform(x_blim, x_ulim)
    y_coord = random.uniform(function(x_blim),function(x_ulim))
    
    if y_coord < function(x_coord):
        in_area += 1
    
    count += 1

#counts how many dots fall within region below graph
ans = (in_area / count)*((x_ulim-x_blim)*(function(x_ulim))-function(x_blim))
print(ans)
