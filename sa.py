import random 
import math
def cost(x): return x*x

def simulated_annealing(start,temp,cooling,steps):
    x=start
    for _ in range(steps):
        next_x= x +  (random.random()-0.5)/2
        if cost(x)> cost(next_x) or math.exp((cost(x)-cost(next_x))/temp)>random.random():
            x=next_x
        temp*=cooling
        if temp< 1e-8:
            break
    return x

result=simulated_annealing(10,1000,0.99,10000)
print(f"Mininmum  at x {result} ,f(x)= {result *result}")