class locationClass:
	def __init__(self, name = 'undefined', genericdescription = 'undefined', cardDeck = [], locationLinks = None):
		self.__name__ = name
		self.__genericdescription__ = genericdescription
		self.__cardDeck__ = cardDeck
		self.__timesVisited__ = 0
		self.__locationLinks__ = locationLinks
	def getName(self):
		return self.__name__
	def addLocationLink(self, link):
		if self.__locationLinks__ == None:
			self.__locationLinks__ = []
		self.__locationLinks__.append(link)
	def dealCard(self): 
		pass
		#should deal a generic card if no cards in deck
	def visit(self, player):
		__player__ = player
		self.__timesVisited__ += 1
		if self.__locationLinks__ = None:
			self.dealCard()
	def getGenericDesc(self):
		return self.__genericdescription__
	def getFullDesc(self):
		return self.__genericdescription__