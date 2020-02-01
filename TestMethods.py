""" Creation of test methods for sheep vaccination schemas """

def simpletest(flock):
    """ Return number of test required for testing the sheep flock """
    n = 0
    sheeps = flock.sheep
    while len(sheeps) > 0:
        n += 1
        testgroup = sheeps[0:5]
        testResult = test(testgroup)
        
        if testResult:
            n += 5
        
        del sheeps[0:4]
    
    return n
        
def test(group):
    
    result = False
    
    for sheep in group:
        if sheep.sick:
            result = True
            break

    return result
    