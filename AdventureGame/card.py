class card:
	def __init__(self, cardText, actionsList):
		self.__numberTimesDealt__ = 0
		self.__cardText__ = cardText
		self.__actionsList__ = actionsList
	def getCardText(self):
		return self.__cardText__
	def getActionsList(self):
		return self.__actionsList__
	def getNumberTimesDealt(self):
		return __numberTimesDealt__



