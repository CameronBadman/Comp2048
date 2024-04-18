# -*- coding: utf-8 -*-
"""
The Game of Life (GoL) module named in honour of John Conway

This module defines the classes required for the GoL simulation.

Created on Tue Jan 15 12:21:17 2019

@author: shakes
"""
import numpy as np
from scipy import signal
import rle

class GameOfLife:
    '''
    Object for computing Conway's Game of Life (GoL) cellular machine/automata
    '''
    def __init__(self, N=256, finite=False, fastMode=False):
        self.grid = np.zeros((N,N), np.int64)
        self.neighborhood = np.ones((3,3), np.int64) # 8 connected kernel
        self.neighborhood[1,1] = 0 #do not count centre pixel
        self.finite = finite
        self.fastMode = fastMode
        self.aliveValue = 1
        self.deadValue = 0
        
    def getStates(self):
        '''
        Returns the current states of the cells
        '''
        return self.grid
    
    def getGrid(self):
        '''
        Same as getStates()
        '''
        return self.getStates()
               
    def evolve(self):
        '''
        Given the current states of the cells, apply the GoL rules:
        - Any live cell with fewer than two live neighbors dies, as if by underpopulation.
        - Any live cell with two or three live neighbors lives on to the next generation.
        - Any live cell with more than three live neighbors dies, as if by overpopulation.
        - Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction
        '''
        
        # Calculate the weighted sum of neighbors
        
      
        # Apply the Game of Life rules
        # A live cell with 2 or 3 live neighbors stays alive, else it dies
        # A dead cell with exactly 3 live neighbors becomes alive
        
        #get weighted sum of neighbors
        #PART A & E CODE HERE
         
        # EXPLANATION 
        # convolve is a function that takes multiple argument, but the main 2 are a 2 np.arrays
        # the first np.array is the base array (self.grid)
        # the second array is the kernal np.array, this is the values that the valeus found in self.grid are multiplied times 
        # for example 
        #
        # [0, 1, 0]
        # [0, 1, 0] convolve [1, 1]
        # [0, 1, 0]          [1, 1]

        # for example operation 5 in this sequence would be would be sum([[1, 0],[0, 1]] * [[1, 1],[1,1]]) = 2 so on
        # the next arguement is boundary which I set to  wrap if infinite and fill if finite, this means that when convolve prospectivly goes over the np.array,
        # it will assume they are the fillvaue (fill), or go to the oppposite of the np.array to get the value (wrap)
        # thus a glider that goes off the bottom right of the screen will show up at the top left

        # mode = 'same' means that the array put in will get the same sized output, making it easyer to go over with np.where

        # finnaly the fill value fill the intial np,array with values, for which the numbers are then placed in, these also are the default values for when the kernal is over the edge 
        # of the grid

        
        
        # gets the amount of neighbors using convovle
        neighbor_count = signal.convolve2d(self.grid, self.neighborhood, mode='same', boundary='wrap' if not self.finite else 'fill', fillvalue=self.deadValue)


        # EXPLANATION 
        # the np.where function is useful for elegeantly placing values into a array, using arrays of similar sizing.
        # The reasoning for using this is to speed up the N as much as possible by using np.arrays to ensure speed,
        # and using a inbuilt numpy library also comes with speed optimisation out of the box for most use cases
        # using the neibor_count function, which implicitly would clear all cells, the cells that fit rules 2 and 4 are activated creating life 
        # thus meaning that 1 and 3 are implicitly done the completly clearing the grid


        # executes rule 2
        self.grid = np.where((self.grid == self.aliveValue) & ((neighbor_count == 2) | (neighbor_count == 3)), self.aliveValue, self.deadValue)
        # executes rule 4
        self.grid = np.where((self.grid == self.deadValue) & (neighbor_count == 3), self.aliveValue, self.grid)
    

        # debuging and code for understand conways game visually by terminal 
        """ 
        print("-"*100 + " grid")
        for row in self.grid:
            print(' '.join(map(str, row)))
        print("-"*100 + " neighborhood")
        for row in neighbor_count:
            print(' '.join(map(str, row)))

        """
        
        #implement the GoL rules by thresholding the weights
        #PART A CODE HERE
        
        #update the grid
#        self.grid = #UNCOMMENT THIS WITH YOUR UPDATED GRID
    
    def insertBlinker(self, index=(0,0)):
        '''
        Insert a blinker oscillator construct at the index position
        '''
        self.grid[index[0], index[1]+1] = self.aliveValue
        self.grid[index[0]+1, index[1]+1] = self.aliveValue
        self.grid[index[0]+2, index[1]+1] = self.aliveValue
        
    def insertGlider(self, index=(0,0)):
        '''
        Insert a glider construct at the index position
        '''  
        self.grid[index[0], index[1]+1] = self.aliveValue
        self.grid[index[0]+1, index[1]+2] = self.aliveValue
        self.grid[index[0]+2, index[1]] = self.aliveValue
        self.grid[index[0]+2, index[1]+1] = self.aliveValue
        self.grid[index[0]+2, index[1]+2] = self.aliveValue
        
    def insertGliderGun(self, index=(0,0)):
        '''
        Insert a glider construct at the index position
        '''
        self.grid[index[0]+1, index[1]+25] = self.aliveValue
        
        self.grid[index[0]+2, index[1]+23] = self.aliveValue
        self.grid[index[0]+2, index[1]+25] = self.aliveValue
        
        self.grid[index[0]+3, index[1]+13] = self.aliveValue
        self.grid[index[0]+3, index[1]+14] = self.aliveValue
        self.grid[index[0]+3, index[1]+21] = self.aliveValue
        
        self.grid[index[0]+3, index[1]+35] = self.aliveValue
        self.grid[index[0]+3, index[1]+36] = self.aliveValue
        
        self.grid[index[0]+4, index[1]+12] = self.aliveValue
        self.grid[index[0]+4, index[1]+16] = self.aliveValue
        self.grid[index[0]+4, index[1]+21] = self.aliveValue

        self.grid[index[0]+3, index[1]+22] = self.aliveValue

        self.grid[index[0]+6, index[1]+18] = self.aliveValue
        
        self.grid[index[0]+4, index[1]+22] = self.aliveValue
        self.grid[index[0]+4, index[1]+35] = self.aliveValue
        self.grid[index[0]+4, index[1]+36] = self.aliveValue
        
        self.grid[index[0]+5, index[1]+1] = self.aliveValue
        self.grid[index[0]+5, index[1]+2] = self.aliveValue
        self.grid[index[0]+5, index[1]+11] = self.aliveValue
        self.grid[index[0]+5, index[1]+17] = self.aliveValue
        self.grid[index[0]+5, index[1]+21] = self.aliveValue
        self.grid[index[0]+5, index[1]+22] = self.aliveValue
        
        self.grid[index[0]+6, index[1]+1] = self.aliveValue
        self.grid[index[0]+6, index[1]+2] = self.aliveValue
        self.grid[index[0]+6, index[1]+11] = self.aliveValue
        self.grid[index[0]+6, index[1]+15] = self.aliveValue
        self.grid[index[0]+6, index[1]+17] = self.aliveValue
        self.grid[index[0]+6, index[1]+17] = self.aliveValue
        self.grid[index[0]+6, index[1]+23] = self.aliveValue
        self.grid[index[0]+6, index[1]+25] = self.aliveValue
        
        self.grid[index[0]+7, index[1]+11] = self.aliveValue
        self.grid[index[0]+7, index[1]+17] = self.aliveValue
        self.grid[index[0]+7, index[1]+25] = self.aliveValue
        
        self.grid[index[0]+8, index[1]+12] = self.aliveValue
        self.grid[index[0]+8, index[1]+16] = self.aliveValue
        
        self.grid[index[0]+9, index[1]+13] = self.aliveValue
        self.grid[index[0]+9, index[1]+14] = self.aliveValue

    def insertFromPlainText(self, file_name, row=0, col=0):
        """
        Inserts a pattern from a text file into the grid.
        
        Args:
            file_name (str): The name of the file containing the pattern.
            row (int): The starting row index for the pattern.
            col (int): The starting column index for the pattern.
        """
        with open(file_name, 'r') as f:
            rows = [line.strip() for line in f.readlines()]
        
        for i, row_str in enumerate(rows):
            for j, char in enumerate(row_str):
                print(row_str, char)
                if char == '0':
                    print(1)
                    self.grid[row + i, col + j] = self.aliveValue

        print("-"*100 + " grid")
        for row in self.grid:
            print(' '.join(map(str, row)))



    def insertFromRLE(self, rleString, pad=0):
        '''
        Given string loaded from RLE file, populate the game grid
        '''

        