
""" Code for solving project euler problem 1-3 """

############################################
#               Problem 1                  #
############################################

def get_3_5_sum(num):
    """ Generates the sum of all multiples of 3 and 5 below the input number """
    nums = range(num)
    mults = [num for num in nums if (num % 3 == 0 or num % 5 == 0)]
    return sum(mults)

#print(get_3_5_sum(10))
#print(get_3_5_sum(1000))

############################################
#               Problem 2                  #
############################################

def fibbonachi(num):
    """ Returns a list of fibbonachi numbers with value below num """
    a = 1
    b = 2
    fib = [a, b]
    c = a + b
    while c < num:
        fib.append(c)
        a, b = b, c
        c = a + b
    return fib

def even_fibbonachi_sum(num):
    """ Return the sum of all even fibbonachi numbers """
    fibs = fibbonachi(num)
    evenFib = [fib for fib in fibs if (fib % 2 == 0)]
    return sum(evenFib)

#print(even_fibbonachi_sum(4000000))

############################################
#               Problem 3                  #
############################################
def prime_checker(num):
    """ Return True if number is Prime, returns False otherwise """
    if num <= 0:
        return "Error: num must be a positive nonzero integer"
    elif num <= 3:
        return num > 1
    elif num % 2 == 0 or num % 3 == 0:
        return False
    else:
        k = 5
        while k * k < num:
            if (num % k == 0) or (num % (k+2) == 0):
                return False
            k += 6
    return True

""" print(prime_checker(-2))
print(prime_checker(0))
print(prime_checker(117))
print(prime_checker(600851475143)) """


def prime_generator(num):
    """ Create a list of Primes below num """
    prime_list = [i for i in range(1,num+1,2) if prime_checker(i)]

    if num > 1:
        prime_list.insert(0,2)

    return prime_list

#print(prime_generator(100))
    
def prime_factors(num):
    """ Return a list of prime factors for num """
    if prime_checker(num):
        return num
    if num > 10^5:
        maxPrime = round(num**0.5) + 1
    else:
        maxPrime = round(num/2)+1
    primelist = prime_generator(maxPrime)
    factors = []

    while num > 1 and num not in primelist:
        for prime in primelist:
            if num % prime == 0:
                factors.append(prime)
                num = int(num / prime)
                break
    if not num == 1:
        factors.append(num)
    
    return factors
 
""" print(prime_factors(13195))
print(prime_factors(600851475143)) """

############################################
#               Problem 4                  #
############################################

def int2list(num):
    """ Returns a list of intergers in num """
    return [int(d) for d in str(num)]

#print(int2list(1239843))

def is_palindrome(num):
    """ Return True if num is a palindrome number """
    digitList = int2list(num)
    
    i = 0
    while i <= round(len(digitList)/2):
        if digitList[i] != digitList[-(i+1)]:
            return False
        i += 1
    return True

""" print(is_palindrome(112321348234888432425324232))
print(is_palindrome(12345678987654321)) """

def largest_palindrome(num):
    """ Returns the largest palindrome number of two intergers with length of num """
    rangeMax = 10 ** num - 1
    rangeMin = 1
    maxPal = 1
    i = rangeMax

    while i >= rangeMin:
        for j in reversed(range(rangeMin,i+1)):
            if is_palindrome(i * j) and i * j > maxPal:
                maxPal = i * j
                rangeMax = i 
                rangeMin = j
                i -= 1
                break
            if j == rangeMin:
                i -= 1
    return [maxPal, rangeMin, rangeMax]

#print(largest_palindrome(3))

############################################
#               Problem 5                  #
############################################

def smallest_common_divisor(num):
    """ Returns the smallest number who evenly divides all integers from 1 to num """

    minDiv = num * (num-1)
    divisor = minDiv
    num -= 2

    while num > 1:
        if divisor % num == 0:
            num -= 1
            minDiv = divisor
        else:
            divisor += minDiv
    
    return minDiv

""" for i in range(1,20):
    print(smallest_common_divisor(i)) """
print(smallest_common_divisor(20))
