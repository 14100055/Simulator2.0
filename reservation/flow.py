import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from base.traffic import Traffic
from base.path import Path

class Flow(Traffic):
	def __init__(self, _id, _label, _start, _active, _rate, _size, _src, _dst):
		Traffic.__init__(self, _id, _label, _start, _active, _rate, _size)
		self.src = _src
		self.dst = _dst
		self.paths = []
