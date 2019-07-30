#BEGINNING OF PRIME.PY
#work on this when you are done with other work
#
#implement this function, isPrime(n)
#which should return True if n is prime
#and False otherwise
#examples:
#   isPrime(1) returns False
#   isPrime(5) returns True
#   isPrime(28) returns False
#

#def isPrime(n):
    #replace this return statement with your code
#    return False


#implement generatePrimes(n)
#which should return a list containing all the primes up to n
#Examples:
#   generatePrimes(1) should return []
#   generatePrimes(5) should return [2,3,5]
#   generatePrimes(20) should return [2,3,5,7,11,13,17,19]
#def generatePrimes(n):
#    return []

#END OF PRIME.PY
#n=int(input("input number"))
#c=[]

#for i in range(2,n):
##    for k in range(2,i):
#        if (i%k)==0:
#            break
#    else:
#        print(i)


n=int(input("input number"))
c=[]

for i in range(2,n):
    for k in range(2,i):
        if (i%k)==0:
            break
    else:
        print(i)
