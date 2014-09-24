import device
import link
# import traffic
# import flow
# import tenant

"""
eventType = "Failure" or "Recovery" or "TenantArrival" or "FlowArrival"
"""

class Event:
	def __init__(self, _id, _time, _eventType):
		self.id = _id
		self.time = _time
		self.eventType = _eventType

	def getEventID(self):
		return self.id
	def getEventTime(self):
		return self.time
	def getEventType(self):
		return self.eventType


class FailureEvent(Event):
	def __init__(self, _id, _time, _eventType, _componentType, _object):
		Event.__init__(self, _id, _time, _eventType)
		self.componentType = _componentType
		self.failingDevice = _object
		self.failingLink = _object
		if _componentType == 'device':
			self.failingLink = None
		elif _componentType == 'link':
			self.failingDevice = None
		else:
			print 'Error in creating failure event'

	def getComponentType(self):
		return self.componentType
	def getComponent(self):
		if self.componentType == 'device':
			return self.failingDevice
		else:
			return self.failingLink
	def printInfo(self):
		print '=========================='
		print 'ID:        ' + str(self.id)
		print 'Time:      ' + str(self.time)
		print 'Event:     ' + self.eventType
		print 'Component: ' + self.componentType
		print '=========================='


class RecoveryEvent(Event):
	def __init__(self, _id, _time, _eventType, _componentType, _object):
		Event.__init__(self, _id, _time, _eventType)
		self.componentType = _componentType
		self.recoveringDevice = _object
		self.recoveringLink = _object
		if _componentType == 'device':
			self.recoveringLink = None
		elif _componentType == 'link':
			self.recoveringDevice = None
		else:
			print 'Error in creating recovery event'

	def getComponentType(self):
		return self.componentType
	def getComponent(self):
		if self.componentType == 'device':
			return self.recoveringDevice
		else:
			return self.recoveringLink


class TenantArrivalEvent(Event):
	def __init__(self, _id, _time, _eventType, _vms, _bw, _data, _start, _duration):
		Event.__init__(self, _id, _time, _eventType)
		self.VMs = _vms
		self.BW = _bw
		self.data = _data
		self.start = _start
		self.duration = _duration


class FlowArrivalEvent(Event):
	def __init__(self, _id, _time, _eventType, _bw, _data, _start, _duration):
		Event.__init__(self, _id, _time, _eventType)
		self.BW = _bw
		self.data = _data
		self.start = _start
		self.duration = _duration
