def CheckIfPrime(number):

    if number == 1:
        return True
        
    for x in range(2,number+1):
        if number > x:
            if number%x==0:
                return False
            continue
        else:
            return True