import math
import sys
from random import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from msModel import *

class msView(QWidget):
	def __init__(self):
		super(msView, self).__init__()
		self.model = msModel() #create an instance of model class
		self.cleared = 0 
		self.layoutA = QVBoxLayout() #create a layout
		self.layoutB = QHBoxLayout() #another layout
		self.gridLayout = QGridLayout() 
		self.bombCount = QLabel("Bomb Count: "+str(self.model.bombCount))
		self.moveCount = QLabel("Move Count: "+str(self.cleared))
		self.layoutA.addWidget(self.bombCount) #add labels to first layout
		self.layoutA.addWidget(self.moveCount)
		self.setLayout(self.layoutA)
		self.layoutA.addLayout(self.layoutB) #add secondary layout to primary layout
		self.layoutB.addLayout(self.gridLayout) #add the grid
		self.setStyleSheet("background-color: darkCyan;")
		self.setWindowTitle('Minesweeper')
		print(self.model.boardArr)

		for x in range(self.model.boardSize): #create a 2D array of buttons
			for y in range(self.model.boardSize):
				self.button = QPushButton("", self)
				self.button.setProperty("myRow", y) #provide coordinate references for button
				self.button.setProperty("myCol", x)
				self.button.setFixedSize(50,50)
				self.gridLayout.addWidget(self.button, x, y)
				self.button.clicked.connect(self.onClick) #connect button to function
				if(self.model.boardArr[x][y] == 1):
					self.button.clicked.connect(self.gameOver)
					self.button.clicked.connect(self.close)
		
	def onClick(self):
		clicked = self.sender() #set signal sender
		x = clicked.property("myCol")
		y = clicked.property("myRow") #grab coordinates from clicked button
		cellInfo = self.model.reveal(x,y) #pass to reveal
		self.buttonC = QPushButton("", self) #create a replacement button
		self.buttonC.setProperty("myCol", x)
		self.buttonC.setProperty("myRow", y)
		self.buttonC.setFixedSize(50,50)
		self.gridLayout.addWidget(self.buttonC, x, y) #drop in new button
		self.buttonC.setText(str(cellInfo)) #get info from reveal and update button
		self.cleared+=1 #cleared cells count
		self.moveCount.setText("Move Count: " + str(self.cleared)) #updating external label
		self.buttonC.setStyleSheet("QPushButton" #do some style stuff on button-click
                             "{"
                             "background-color : Green;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : red;"
                             "}"
                             )

		if(self.cleared == ((self.model.boardSize**2) - self.model.bombCount)): #win condition
			messageRand = randint (1,3)
			if(messageRand == 1):
				print("Mines cleared. You won!")
			if(messageRand == 2):
				print("Well done, soldier!")
			if(messageRand == 3):
				print("Victory achieved.")
			self.close()
		# print("Coordinates: "+str(x),str(y))
		# print("Moves made: "+str(self.cleared))

	def gameOver(self): #loss state
		messageRand2 = randint (1,4)
		if(messageRand2 == 1):
			print("You lost.")
		if(messageRand2 == 2):
			print("BOOM! ...you lost.")
		if(messageRand2 == 3):
			print("You explode into a million little pieces.")
		if(messageRand2 == 4):
			print("THE HORROR!")

		self.close()