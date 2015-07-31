def is_pallindrome(n):
    if str(n) == str(n)[::-1]:
            return True    
    return False

largest = 0
for i in range(100, 1000):
    for j in range(i, 1000):
        if is_pallindrome(i*j):
            if (i*j) > largest: largest = i*j
print largest

