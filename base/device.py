from component import Component
import link

class Device(Component):
	def __init__(self, _id, _label, _isHost):
		Component.__init__(self, _id, _label)
		self.compType = 'device'
		self.isHost = _isHost
		self.VMs = 0
		if _isHost:
			self.VMs = 4
		self.availableVMs = self.VMs
		self.links = []

# Setter functions
	def addLink(self, link):
		self.links.append(link)

	def removeLink(self, link):
		self.links.remove(link)

# Getter functions
	def getAvailableVMs(self):
		return self.availableVMs

	def getNumPorts(self):
		return len(self.links)

	# this is only for host devices
	def getLink(self):
		return self.links[0]

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
		