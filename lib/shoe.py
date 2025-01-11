#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand= "Adidas",size = 9):
        self._brand = brand
        self._size =size
        self._condition = "Old"
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self,value):
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")



    @property
    def brand(self):
        return self._brand
    
    @brand.setter
    def brand(self,value):
        self._brand = value

    @property
    def condition(self):
        return self._condition
    
    def cobble(self):
        print("Your shoe is as good as new!")
        self._condition = "New"