import os
import card
import textwrap
import math

class screendisplay:
	def __init__(self, **kwargs):
		self.displayColumns = os.get_terminal_size().columns
		self.displayLines = os.get_terminal_size().lines
		self.currTextPage = 0
		self.totalTextPages = 0
		self.currActionPage = 0
		self.displayText = "Uninitialized Card Text"
		self.possibleActions = []
		self.tw = textwrap.TextWrapper(self.displayColumns)
		self.textBlockSize = self.displayLines - 3
		return super().__init__(**kwargs)
	def loadCard(self,gotcard):
		self.currentCard = gotcard
	def formatDisplayText(self,text):
		self.displayText = self.tw.wrap(text)
		self.currTextPage = 0
		self.totalTextPages = math.ceil(len(self.displayText)) - 1
	def formatDisplayActions(self):
		pass
	def prntScreen(self):
		os.system('cls')
		foo = 0
		for each in self.displayText[(self.currTextPage * self.textBlockSize):(self.currTextPage + 1) * self.textBlockSize]:
			print(each)
			foo += 1
		while foo < self.textBlockSize :
			print()
			foo += 1
		if self.currTextPage != self.totalTextPages:
			def nextPage():
				self.currTextPage += 1
				self.prntScreen()
			if self.possibleActions != [] : 
				self.possibleActions.clear()
			self.possibleActions.append(['NextPage',nextPage])  # next bit should deal with resetting correct actions from card if no next page
		else: 
			self.formatDisplayActions()
		for each in self.possibleActions:
			print(each[0])
