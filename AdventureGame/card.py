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
	def beDealt(self, player):
		self.__numberTimesDealt__ += 1
		self.__player__ = player
		return self


	#Need to create a generic location card, with a return to Home and any basic action/inventory buttons.  Shows current location description & basic actions, other locations

	#Generic card: You are lost in the mists.  Generic actions + gohome