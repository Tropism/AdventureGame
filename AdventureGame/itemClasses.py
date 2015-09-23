class genericItem:
	def __init__(self, label = 'nullitem', description = 'nulldesc', value = 0):
		self.__label__ = label
		self.__description__ = description
		self.__value__ = value
	def getDesc(self):
		return self.__description__
	def getLabel(self):
		return self.__label__
	def getValue(self):
		return self.__value__