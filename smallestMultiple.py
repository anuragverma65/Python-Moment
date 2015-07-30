def calculate(num, current_lcm = 1):
    if (num == 1): return current_lcm
    return calculate(num - 1, lcm(num, current_lcm))

def lcm(a, b):
    return a * b // gcd(a, b)

def gcd(a, b):
    while b:      
        a, b = b, a % b
    return a

print calculate(20)
