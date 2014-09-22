import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from base.traffic import Traffic

class Flow(Traffic):
	def __init__(self, _id, _label, _start, _active, _rate, _size, _vms, _bw):
		Traffic.__init__(self, _id, _label, _start, _active, _rate, _size)
		self.VMs = _vms
		self.BW = _bw
		self.hosts = []
		self.links = []
