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
import random


class GameOfLife:
    '''
    Object for computing Conway's Game of Life (GoL) cellular machine/automata
    '''
    def __init__(self, N=256, finite=False, fastMode=False):
        self.grid = np.zeros((N,N), np.byte)
        self.neighborhood = np.ones((3,3), np.byte) # 8 connected kernel
        self.neighborhood[1,1] = 0 #do not count centre pixel
        self.finite = finite
        self.fastMode = fastMode
        self.aliveValue = 1
        self.deadValue = 0
        self.size = N
        
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
    
    def get_grid_val(self, offset, position):
            return self.grid[offset[0] + position[0]][offset[1] + position[1]]
    
    def slow_evolve(self, mode='same', boundary="wrap"):
        """
        A slow implementation of the Game of Life evolution algorithm.

        This function calculates the number of live neighbors for each cell in the grid
        based on the current state of the grid and the neighborhood kernel.

        Args:
            mode (str, optional): Determines the output shape. {'full', 'valid', 'same'}
                Default is 'same'.
            boundary (str, optional): Determines how to handle boundaries. {'wrap', 'fill'}
                Default is 'wrap'.

        Returns:
            numpy.ndarray: A 2D array of the same shape as the grid, where each element
                represents the number of live neighbors for the corresponding cell.
        """
        # Mimic behavior based on boundary
        if boundary == 'wrap':
            # Pad the grid with wrapped edges
            padded_grid = np.pad(self.grid, 1, mode='wrap')
        else:
            # 'fill'
            # Pad the grid with dead cells
            padded_grid = np.pad(self.grid, 1, mode='constant', constant_values=self.deadValue)

        # Calculate the weighted sum of neighbors based on the neighborhood kernel
        neighbor_count = np.zeros_like(self.grid)
        for row in range(1, self.size + 1):
            for col in range(1, self.size + 1):
                # Calculate the sum of neighbors for the current cell
                neighbor_count[row-1, col-1] = np.sum(padded_grid[row-1:row+2, col-1:col+2] * self.neighborhood)

        return neighbor_count
    
    def fast_evolve(self):
        """
        Perform a fast evolution of the grid using convolution.

        This method uses convolution to evolve the grid to the next generation.
        Convolution is a mathematical operation that applies a filter (kernel)
        to an input array (base array) to produce an output array.

        Args:
            self.grid (np.array): The base array representing the current generation.
            self.neighborhood (np.array): The kernel array representing the neighborhood pattern.
            self.finite (bool): A flag indicating whether the grid has finite boundaries.

        Returns:
            np.array: The evolved grid representing the next generation.

        Explanation:
            - Convolve is a function that takes multiple arguments, primarily two np.arrays.
            The first np.array is the base array (self.grid), and the second array is the kernel np.array.
            This kernel represents the values that the values found in self.grid are multiplied by.
            For example:
                [0, 1, 0]
                [0, 1, 0] convolve [1, 1]
                [0, 1, 0]          [1, 1]
            For example, operation 5 in this sequence would be sum([[1, 0],[0, 1]] * [[1, 1],[1,1]]) = 2 and so on.
            - The 'boundary' argument is set to 'wrap' if infinite and 'fill' if finite.
            This means that when convolve prospectively goes over the np.array, it will assume they are the fill value (fill),
            or go to the opposite of the np.array to get the value (wrap).
            Thus, a glider that goes off the bottom right of the screen will show up at the top left.
            - 'Mode' set to 'same' means that the array put in will get the same sized output,
            making it easier to go over with np.where.
            - Finally, the fill value fills the initial np.array with values, for which the numbers are then placed in.
            These also are the default values for when the kernel is over the edge of the grid.
        """
        return signal.convolve2d(self.grid, self.neighborhood, mode='same', boundary='wrap' if not self.finite else 'fill', fillvalue=self.deadValue)

        
  
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
              
        neighbor_count = self.fast_evolve() if self.fastMode else self.slow_evolve(boundary='wrap' if not self.finite else 'fill')
        
        # gets the amount of neighbors using convovle
    
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

    
    def insertBlinker(self, index=(0,0)):
        '''
        Insert a blinker oscillator construct at the index position
        '''
        self.grid[index[0], index[1]+1] = self.aliveValue
        self.grid[index[0]+1, index[1]+1] = self.aliveValue
        self.grid[index[0]+2, index[1]+1] = self.aliveValue


    def randomLargePattern(self):
        random_grid = np.zeros_like(self.grid)
        
        for x in range(self.grid.shape[0]): 
            for y in range(self.grid.shape[1]): 
                random_number = random.randint(0, 10)
                #print(random_number)
                if random_number <= 3:
                    random_grid[x,y] = self.aliveValue

        self.grid = random_grid
    
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
        Inserts a pattern from a .cells file into the grid.

        Args:
            file_name (str): The name of the file containing the pattern.
            row (int): The starting row index for the pattern.
            col (int): The starting column index for the pattern.
        """
        with open(file_name, 'r') as f:
            lines = f.readlines()

        # Skip metadata lines (lines starting with '!')
        pattern_lines = [line.strip() for line in lines if not line.startswith('!')]

        for i, row_str in enumerate(pattern_lines):
            for j, char in enumerate(row_str):
                if char == 'O':
                    self.grid[row + i, col + j] = self.aliveValue
                # You may want to add an else condition here to handle other characters



    def insertFromRLE(self, rleString, pad=0):
        '''
        Given string loaded from RLE file, populate the game grid
        '''
        parser = rle.RunLengthEncodedParser(rleString)

        # Iterate over each cell in the pattern
        for y, row in enumerate(parser.pattern_2d_array):
            for x, cell in enumerate(row):
                # Check if the cell is alive
                if cell != 'b':
                    # Calculate the target position in the grid
                    target_y = pad + y
                    target_x = pad + x

                    # Check if the target position is within the bounds of the grid
                    if 0 <= target_y < self.size and 0 <= target_x < self.size:
                        # Set the corresponding cell in the grid to the alive value
                        self.grid[target_y, target_x] = self.aliveValue