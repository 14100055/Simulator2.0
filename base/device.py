import base.link

class Device:
	def __init__(self, _id, _label, _isHost):
		self.id = _id
		self.label = _label
		self.status = True
		self.isHost = _isHost
		self.VMs = 0
		if _isHost:
			self.VMs = 4
		self.availableVMs = self.VMs
		self.links = []

# Setter functions
	def setStatus(self, _status):
		self.status = _status

	def addLink(self, link):
		self.links.append(link)

	def removeLink(self, link):
		self.links.remove(link)

# Getter functions
	def getID(self):
		return self.id;

	def getLabel(self):
		return self.label

	def getStatus(self):
		return self.status

	def getAvailableVMs(self):
		return self.availableVMs

	def getNumPorts(self):
		return len(self.links)

	def getLinks(self):
		return self.links

	# this is only for host devices
	def getLink(self):
		return links[0]

# Utility functions
	def printInfo(self):
		print '=========================='
		print 'ID:       ' + str(self.id)
		print 'Label:    ' + self.label
		print 'Status:   ' + self.status
		if isHost:
			print 'Host device'
		else:
			print 'Switch device'
		print '=========================='
		