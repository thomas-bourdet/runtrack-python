for num in range(2, 1001):
    prime = True
    
    if num < 2:
        prime = False
    
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            prime = False
            break
    
    if prime:
        print(num)
