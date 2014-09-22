import base.device
import base.link
import base.traffic
import base.flow
import base.tenant

"""
eventType = "Failure" or "Recovery" or "TenantArrival" or "FlowArrival"
"""

class Event:
	def __init__(self, _id, _time, _eventType):
		self.id = _id
		self.time = _time
		self.eventType = _eventType


class FailureEvent(Event):
	def __init(self, _id, _time, _eventType, _objectType, _object):
		Event.__init__(self, _id, _time, _eventType)
		self.objectType = _objectType
		self.failingDevice = _object
		self.failingLink = _object
		if _objectType == 'device':
			self.failingLink = None
		elif _objectType == 'link':
			self.failingDevice = None
		else:
			print 'Error in creating failure event'


class RecoveryEvent(Event):
	def __init(self, _id, _time, _eventType, _objectType, _object):
		Event.__init__(self, _id, _time, _eventType)
		self.objectType = _objectType
		self.recoveringDevice = _object
		self.recoveringLink = _object
		if _objectType == 'device':
			self.recoveringLink = None
		elif _objectType == 'link':
			self.recoveringDevice = None
		else:
			print 'Error in creating recovery event'


class TenantArrivalEvent(Event):
	def __init(self, _id, _time, _eventType, _vms, _bw, _data, _start, _duration):
		Event.__init__(self, _id, _time, _eventType)
		self.VMs = _vms
		self.BW = _bw
		self.data = _data
		self.start = _start
		self.duration = _duration


class FlowArrivalEvent(Event):
	def __init(self, _id, _time, _eventType, _bw, _data, _start, _duration):
		Event.__init__(self, _id, _time, _eventType)
		self.BW = _bw
		self.data = _data
		self.start = _start
		self.duration = _duration
