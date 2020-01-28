# Products Class for acme
import pandas as pd
import numpy as np
import random
from random import randint

class Product():
    def __init__(self, name, price=10, weight=20, flammability=.5, identifier=random.randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        """calculates the price divided by the weight, and then
            returns a message: if the ratio is less than 0.5 return "Not so stealable...",
            if it is greater or equal to 0.5 but less than 1.0 return "Kinda stealable.",
            and otherwise return 'Very stealable!'
        """
        ratio = (self.price)/(self.weight)
        if ratio < .5:
            return 'Not so stealable...'
        elif (ratio > .5 and ratio < 1):
            return 'Kinda stealable...'
        else:
            return 'Very stealable!'


    def explode(self):
        """ calculates the flammability times the weight, and then returns a message: if the product is less than 10 return "...fizzle.", if it is greater or equal to 10 but less than 50 return "...boom!", and otherwise return "...BABOOM!!"
        """
        bomb = (self.flammability)*(self.weight)
        if bomb < 10:
            print('...fizzle.')
        elif (bomb > 10 and bomb < 50):
            print('...boom!')
        else:
            print('...BABOOM!!')


class BoxingGlove(Product):
    def __init__(self, name, price=10, weight=10, flammability=.5, identifier=random.randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier
    
    def explode(self):
        """ Override the explode method for the boxing glove product"""
        print("...it's a glove")

    def punch(self):
        """ Returns "That tickles." if the weight is below 5,
            "Hey that hurt!" if the weight is greater or equal to 5 but less than 15, and
            "OUCH!" otherwise
        """
        if self.weight < 5:
            print('That tickles.')
        elif (self.weight > 5 and self.weight < 15):
            print('Hey that hurt!')
        else:
            print('OUCH!')




if __name__ =="__main__":
    #checks
    prod=Product('A Cool Toy')
    print(prod.name)
    print(prod.price)
    print(prod.weight)
    print(prod.flammability)
    print(prod.identifier)
    prod.explode()
    prod.stealability()

    glove = BoxingGlove('Glover')
    print(glove.weight)
    glove.punch()
    glove.explode()
    