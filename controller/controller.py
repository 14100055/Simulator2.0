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
		topology.bfs(topology.devices[0])
	elif topology_type == 'JellyFish' or topology_type == 'j':
		attributes = []
		attributes.append(int(raw_input('Enter value of N: ')))
		attributes.append(int(raw_input('Enter value of k: ')))
		attributes.append(int(raw_input('Enter value of r: ')))
		attributes.append(int(raw_input('Enter value of s: ')))
		topology = Topology('JellyFish', attributes)
	else:
		print 'Not a valid type of topology. Exiting.'