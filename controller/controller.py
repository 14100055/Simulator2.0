import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from topology.topology import Topology

if __name__ == '__main__':
	topology_type = raw_input('Enter the type of topology to create: ')
	if topology_type == 'FatTree' or topology_type == 'f':
		attributes = []
		attributes.append(int(raw_input('Enter value of k: ')))
		topology = Topology('FatTree', attributes)
		print "DEVICESSSSS"
		print len(topology.devices)
		for d in topology.devices:
			d.printInfo()
		path = topology.findPath(topology.devices[0], topology.devices[15])
		topology.devices[len(topology.devices)-1].printInfo()
		print "Results"
		for p in path:
			p.printInfo()
		# topology.bfs()
		topology.devices[len(topology.devices)-1].printInfo()
		print (len(path))
	elif topology_type == 'JellyFish' or topology_type == 'j':
		attributes = []
		attributes.append(int(raw_input('Enter value of N: ')))
		attributes.append(int(raw_input('Enter value of k: ')))
		attributes.append(int(raw_input('Enter value of r: ')))
		attributes.append(int(raw_input('Enter value of s: ')))
		topology = Topology('JellyFish', attributes)
	else:
		print 'Not a valid type of topology. Exiting.'