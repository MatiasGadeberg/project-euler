""" Create sheep class for testing vaccination """
import random

class Sheep:
    def __init__(self,p):
        if random.uniform(0,1) < p:
            self.sick = True
        else:
            self.sick = False

class Flock:
    def __init__(self,n,p):
        self.sheep = [Sheep(p) for i in range(n)]