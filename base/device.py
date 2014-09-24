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

	# Variables used by path finding algorithm
		self.distance = 0 # to find the shortest distance from start node
		self.predecessor = None
		self.color = 'white' # means that this node is not yet explored


# Setter functions
	def setStatus(self, _status):
		self.status = _status

	def addLink(self, link):
		self.links.append(link)

	def removeLink(self, link):
		self.links.remove(link)

	# Functions used by path finding algorithm
	def setDistance(self, _distance):
		self.distance = _distance

	def setPredecessor(self, _predecessor):
		self.predecessor = _predecessor

	def setColor(self, _color):
		self.color = _color
				

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

	def getNeighbours(self):
		neighbours = []
		for link in self.links:
			neighbours.append(link.getOtherDevice(self))
		return neighbours
	
	# this is only for host devices
	def getLink(self):
		return links[0]

	# Functions used by path finding algorithm
	def getDistance(self):
		return self.distance

	def getColor(self):
		return self.color

	def getPredecessor(self):
		return self.predecessor


# Utility functions
	def printInfo(self):
		print '=========================='
		print 'ID:       ' + str(self.id)
		print 'Label:    ' + self.label
		print 'Status:   %s' % self.status
		if self.isHost:
			print 'Host device'
		else:
			print 'Switch device'
		print '=========================='