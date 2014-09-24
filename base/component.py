
class Component:
	def __init__(self, _id, _label):
		self.id = _id
		self.label = _label
		self.status = True
		self.numFailures = -1
		self.compType = None

# Setter functions
	def setStatus(self, _status):
		self.status = _status

	def setFailure(self, num):
		if num == -1:
			self.numFailures = self.numFailures + num
		else:
			self.numFailures = num

	def toggleStatus(self):
		self.status = not self.status

# Getter functions
	def getID(self):
		return self.id;

	def getLabel(self):
		return self.label

	def getStatus(self):
		return self.status

	def getType(self):
		return self.compType

	def getFailure(self):
		return self.numFailures
