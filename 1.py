""" Code for solving project euler problem 1-3 """

#Problem 1
def get_3_5_sum(num):
    """ Generates the sum of all multiples of 3 and 5 below the input number """
    nums = range(num)
    mults = [num for num in nums if (num % 3 == 0 or num % 5 == 0)]
    return sum(mults)

print(get_3_5_sum(10))
print(get_3_5_sum(1000))

#Problem 2
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

print(even_fibbonachi_sum(4000000))

#Problem 3
def prime_generator(numMax):
    """ Create a list of Primes below num """
    primelist = [1, 2, 3, 5]
    for num in range(6, numMax+1):
        for i in range(2, num//2):
            if num % i == 0:
                break
            primelist.append(num)
    return primelist

print(prime_generator(100))
