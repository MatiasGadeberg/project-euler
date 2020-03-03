""" 
Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525) are bouncy. In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.

Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers is equal to 90%.

Find the least number for which the proportion of bouncy numbers is exactly 99%.
 """

def is_increasing(num):
    num = str(num)
    previousdigit = int(num[0])
    for digit in num[1:]:
        if int(digit) < previousdigit:
            return False
        previousdigit = int(digit)
    
    return True

def is_decreasing(num):
    num = str(num)
    previousdigit = int(num[0])
    for digit in num[1:]:
        if int(digit) > previousdigit:
            return False
        previousdigit = int(digit)
    
    return True

def is_bouncy(num):
    if not is_increasing(num) and not is_decreasing(num):
        return True
    return False

fraction = 0
num = 0
bouncy = 0
while fraction < 0.99:
    num += 1
    if is_bouncy(num):
        bouncy += 1
    fraction = bouncy/num

print(num)



