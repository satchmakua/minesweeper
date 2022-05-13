# CS 224
# Satchel Hamilton
# Project 2 - Minesweeper

import math
import sys
from random import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class msModel:
	def __init__(self):
		super(msModel, self).__init__()
		self.newGame()

	def newGame(self):
		self.boardSize = int(input("Board size is value squared: ")) #set board size and bomb count
		self.bombCount = self.boardSize #bombcount will be sqrt(boardsize)
		bCount = self.bombCount
		rows, cols = (self.boardSize, self.boardSize)
		self.boardArr = [[0 for i in range(cols)] for j in range(rows)] #create 2D backend array rep

		while bCount > 0: #randomly set bomb positions
			self.boardArr[randint(0,(self.boardSize-1))][randint(0,(self.boardSize-1))] = 1
			bCount-=1

	def reveal(self,i,j): #uses multiple checks to avoid negative indexing and out-of-bounds errors
		self.bombAdj = 0
		self.noBombs = 0
		if(i < (self.boardSize-1)): #checks for various types of adjacency
			if (self.boardArr[i+1][j] == 1):
				self.bombAdj+=1 #increases bomb count if a bomb is found
		if(j < (self.boardSize-1)):
			if (self.boardArr[i][j+1] == 1):
				self.bombAdj+=1
		if(i > 0):
			if (self.boardArr[i-1][j] == 1):
				self.bombAdj+=1
		if(j > 0):
			if (self.boardArr[i][j-1] == 1):
				self.bombAdj+=1
		if(i < (self.boardSize-1) and j < (self.boardSize-1)):
			if (self.boardArr[i+1][j+1] == 1):
				self.bombAdj+=1
		if(i > 0 and j < (self.boardSize-1)):		
			if (self.boardArr[i-1][j+1] == 1):
				self.bombAdj+=1
		if(j > 0 and i < (self.boardSize-1)):
			if (self.boardArr[i+1][j-1] == 1):
				self.bombAdj+=1
		if(i > 0 and j > 0):
			if (self.boardArr[i-1][j-1] == 1):	 
				self.bombAdj+=1
		if(self.bombAdj != 0): #if there are bombs adjacent to cell
			return self.bombAdj #show how many bombs
		else:
			self.noBombs = 1
			self.bombAdj = " " #otherwise leave it blank
			return self.bombAdj
			



