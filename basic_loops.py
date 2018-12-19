from basic_loops_functions import CheckIfPrime 

isPrime=False
show=""
prime=""

for i in range(1,101,1):
    
    if i%3==0 and i%5==0:
        show=" : FizzBuzz"

    elif i%3==0:
        show=" : Fizz"

    elif i%5==0:
        show=" : Buzz"
    
    else:
        show=" :   -  "

    if CheckIfPrime(i):
        prime=" : Prime"
    else:
        prime=" :   -  "

    print(str(i) + prime + show)