import copy
import random
import re

# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        arguments = []
        # print("kwargs: ", kwargs)
        for color, value in kwargs.items():
            for x in range(value):
                arguments.append(color)
        self.contents = arguments
        # print(arguments)
    
    def draw(self, amount):
        if amount > len(self.contents):
            return self.contents
        else:
            # print("all items before we remove them: ", self.contents, len(self.contents))
            removedItems = []
            number = 0
            # random.seed() #this ensures every new random number will be truely random --> if seed(0) > everytime it will remove the zeroth element
            while number < amount and self.contents:
                allballs = len(self.contents)
                rand_int = random.randint(0, allballs-1)
                # print("random integer: ", rand_int)
                toremove = self.contents[rand_int]
                removedItems.append(toremove)
                self.contents.remove(toremove)
                number += 1
            # print("removed items: ", removedItems, len(removedItems), "current items: ", self.contents, len(self.contents))
            return removedItems

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    experiment = 0
    favorable = 0
    while experiment < num_experiments:
        # record the content of hat before doing experiment
        initial = copy.deepcopy(hat.contents)
        # start recording the number each color appears in the removed balls
        drawnBalls = hat.draw(num_balls_drawn)
        counts = dict()
        for ball in drawnBalls:
            counts[ball] = counts.get(ball, 0) + 1
        
        enoughBalls = True
        for color, value in expected_balls.items():
            try:
                if counts[color] < value:
                    enoughBalls = False
                    break
            except:
                enoughBalls = False
                
        if enoughBalls:
            favorable += 1
        # set the contents to original value before performing the next experiment
        hat.contents = initial
        experiment += 1
    
    probability = favorable / num_experiments
    return probability
