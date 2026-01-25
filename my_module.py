data = [2,3,3,23,4,234,24,23,42,43]

def is_prime(n:int)->bool:
    '''check prime'''
    if n<=1:
        return False
    else:
        for d in range(2,n):
            if n%d ==0:
                return False
    return True 