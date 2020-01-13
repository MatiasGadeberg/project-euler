""" Code for solving project euler problem 1 """

def get_3_5_sum(num):
    """ Generates the sum of all multiples of 3 and 5 below the input number """
    nums = range(num)
    mults = [num for num in nums if (num % 3 == 0 or num % 5 == 0)]
    return sum(mults)

print(get_3_5_sum(10))
print(get_3_5_sum(1000))