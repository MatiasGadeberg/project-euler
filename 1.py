
""" Code for solving project euler problem 1-6 """

############################################
#          Problem 1 - Solved              #
############################################

def get_3_5_sum(num):
    """ Generates the sum of all multiples of 3 and 5 below the input number """
    nums = range(num)
    mults = [num for num in nums if (num % 3 == 0 or num % 5 == 0)]
    return sum(mults)

#print(get_3_5_sum(10))
#print(get_3_5_sum(1000))

############################################
#          Problem 2 - Solved              #
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
#          Problem 3 - Solved              #
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
#          Problem 4 - Solved              #
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
#          Problem 5 - Solved              #
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
#print(smallest_common_divisor(20))

############################################
#          Problem 6 - Solved              #
############################################

def sum_square_diff(num):
    """ Returns the difference between the sum of squares of numbers from 1 to num and the square of the sum of the same numbers
        ie. sum_square_diff(num) = sum(i^2 for i in range(1,num+1)) - (sum(i for i in range(1, num+1)))^2"""

    squaresum = sum(range(1,num+1))**2
    squares = [i**2 for i in range(1,num+1)]
    summedsquares = sum(squares)

    return  squaresum - summedsquares

#print(sum_square_diff(10))
#print(sum_square_diff(100))

############################################
#       Problem 7 - Not Solved             #
############################################

def nth_prime(n):
    """ Returns the n'th prime """

    nprime = 0
    prime = 0
    num = 1

    while nprime != n:
        if prime_checker(num):
            nprime += 1
            prime = num
        num += 1
    return prime


""" print(nth_prime(10001))
print(nth_prime(10001-1))
print(nth_prime(10001+1)) """

############################################
#           Problem 8 - Solved             #
############################################

largeNum = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450

def prod_of_consecutive_numbers(num, n):
    """ Returns the largest product of n consecutive numbers from the large number num """
    digitList = int2list(num)
    
    prod = [1] * (n+1)
    for i in range(len(digitList)-n):
        sub = digitList[i:i+n]
        subProd = 1
        for digit in sub:
            subProd = subProd * digit
        if subProd > prod[-1]:
            prod = sub
            prod.append(subProd)
    
    return prod

#print(prod_of_consecutive_numbers(largeNum,4))
#print(prod_of_consecutive_numbers(largeNum,13))