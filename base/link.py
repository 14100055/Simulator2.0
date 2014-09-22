import base.device

class Link:
	def __init__(self, _id, _label, _cap, _device1, _device2):
		self.id = _id
		self.label = _label
		self.status = True
		self.totalCap = _cap
		self.availableCapUp = 0
		self.availableCapDown = 0
		self.device1 = _device1
		self.device2 = _device2
		self.flows = []

# Setter functions
	def setStatus(self, _status):
		self.status = _status

	def setUpBW(self, _up):
		self.availableCapUp += _up

	def setDownBW(self, _down):
		self.availableCapDown += _down

# Getter functions
	def getID(self):
		return self.id;

	def getLabel(self):
		return self.label

	def getStatus(self):
		return self.status

	def getDownSwitch(self):
		return self.device1

	def getUpSwitch(self):
		return self.device2

	def getOtherDevice(self, deviceName):
		if self.device1 == deviceName:
			return self.device2
		if self.device2 == deviceName:
			return self.device1

# Utility functions
	def printInfo(self):
		print '=========================='
		print 'ID:       ' + str(self.id)
		print 'Label:    ' + self.label
		print 'Status:   ' + str(self.status)
		print 'Device 1: ' + str(self.device1)
		print 'Device 2: ' + str(self.device2)
		print 'Capacity: ' + str(self.totalCap)
		print 'Up Cap:   ' + str(self.availableCapUp)
		print 'Down Cap: ' + str(self.availableCapDown)
		print '=========================='
