import sys, os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from base.device import Device
from base.link import Link

import random

class Topology:
	def __init__(self, _topologyType, attributes):
		self.topologyType = _topologyType
		self.devices = []
		self.links = []
		self.generateTopology(_topologyType, attributes)

	def getDevices(self):
		return self.devices
	def getLinks(self):
		return self.links
	def setDevices(self, _devices):
		self.devices = _devices
	def setLinks(self, _links):
		self.links = _links
	def getHosts(self):
		hosts = []
		for device in self.devices:
			if device.getLabel() == 'host':
				hosts.append(device)
		return hosts


	def generateTopology(self, topologyType, attributes):
		if topologyType == 'FatTree':
			self.generateFatTree(attributes);
		if topologyType == 'JellyFish':
			self.generateJellyFish(attributes);


	def generateFatTree(self, attributes):
		k = attributes[0]
		print 'Generating ' + str(k) + '-ary FatTree topology'

		# make sure that k is an even number
		assert(k%2 == 0)

		cores = []
		aggrs = []
		tors = []
		hosts = []

		# add (k/2)^2 cores
		for c in range(k*k/4):
			coreName = 'c' + str(c+1)
			core = Device(coreName, 'core', False)
			cores.append(core)
		
		# add pods with k/2 aggrs and k/2 tors, with k/2 hosts per tor
		for pod in range(k):
			for sw in range(k/2):
				aggrName = 'a_' + str(pod+1) + '_' + str(sw+1)
				torName = 't_' + str(pod+1) + '_' + str(sw+1)
				aggr = Device(aggrName, 'aggr', False)
				tor = Device(torName, 'tor', False)
				for h in range(k/2):
					hostName = 'h_' + str(pod+1) + '_' + str(sw+1) + '_' + str(h+1)
					host = Device(hostName, 'host', True)
					hostLink = Link(h, 'torLink', 1000, host, tor)
					host.addLink(hostLink)
					tor.addLink(hostLink)
					hosts.append(host)
					self.links.append(hostLink)
				aggrs.append(aggr)
				tors.append(tor)

		# connecting tor and aggr switches
		for i in range(k):
			for j in range(k/2):
				for l in range(k/2):
					torLink = Link(l, 'aggrLink', 1000, tors[k/2*i+j], aggrs[k/2*i+l])
					tors[k/2*i+j].addLink(torLink)
					aggrs[k/2*i+l].addLink(torLink)
					self.links.append(torLink)

		# connecting aggr and core switches
		for i in range(k):
			for j in range(k/2):
				for l in range(k/2):
					coreLink = Link(l, 'coreLink', 1000, aggrs[k/2*i+j], cores[j/2*j+l])
					aggrs[k/2*i+j].addLink(coreLink)
					cores[j/2*j+l].addLink(coreLink)
					self.links.append(coreLink)

		# populate devices list
		for host in hosts:
			self.devices.append(host)
		for tor in tors:
			self.devices.append(tor)
		for aggr in aggrs:
			self.devices.append(aggr)
		for core in cores:
			self.devices.append(core)


	def generateJellyFish(self, attributes):
		N = attributes[0]
		k = attributes[1]
		r = attributes[2]
		s = attributes[3]
		# seed(s)
		print 'Generating RRG(' + str(N) + "," + str(k) + "," + str(r) + ') Jellyfish topology'

		numServers = N(k-r)
		# make sure that there are at least as many switches as servers
		assert(N >= numServers)
		# make sure that number of ports per switch is greater than 1
		assert(k > 1)

		# add the servers
		servers = []
		for i in range(numServers):
			hostName = 'h_' + str(i+1)
			host = Device(hostName, 'host', True)
			servers.append(host)

		# add the switches
		switches = []
		openPorts = []
		for i in range(N):
			switchName = 'tor_' + str(i+1)
			switch = Device(switchName, 'tor', False)
			switches.append(switch)
			openPorts.append(k)

		# connect each server with a switch
		for i in range(numServers):
			hostLink = Link(i, 'hostLink', 1000, servers[i], switches[i])
			servers[i].addLink(hostLink)
			switches[i].addLink(hostLink)
			self.links.append(hostLink)
			openPorts[i] -= 1

		# manage the potential links, fully populate the set before creating
		switchesLeft = N
		consecFails = 0

		while switchesLeft > 1 and consecFails < 10:
			s1 = rangrange(N)
			while openPorts[s1] == 0:
				s1 = rangrange(N)
			s2 = rangrange(N)
			while openPorts[s2] == 0 or s1 == s2:
				s2 = rangrange(N)

			torLink1 = Link(s1.getID(), 'torLink', 1000, switches[s1], switches[s2])
			torLink2 = Link(s2.getID(), 'torLink', 1000, switches[s2], switches[s1])
			if torLink1 in self.links or torLink2 in self.links:
				consecFails += 1
			else:
				consecFails = 0
				switches[s1].addLink(torLink1)
				switches[s2].addLink(torLink1)
				self.links.append(torLink1)
				openPorts[s1] -= 1
				openPorts[s2] -= 1
				if openPorts[s1] == 0:
					switchesLeft -= 1
				if openPorts[s2] == 0:
					switchesLeft -= 1

		if switchesLeft > 0:
			for i in range(N):
				while openPorts[i] > 1:
					while True:
						# incremental expansion
						rLink = random.choice(list(links))
						index1 = -1
						index2 = -2
						for i in range(N):
							if switches[i] == rLink.getDownSwitch():
								index1 = i
							if switches[i] == rLink.getUpSwitch():
								index2 = i
						torLink11 = Link(i, 'torLink', 1000, switches[i], switches[index1])
						torLink12 = Link(i, 'torLink', 1000, switches[index1], switches[i])
						if torLink11 in self.links or torLink12 in self.links:
							continue
						torLink21 = Link(i, 'torLink', 1000, switches[i], switches[index2])
						torLink22 = Link(i, 'torLink', 1000, switches[index2], switches[i])
						if torLink21 in self.links or torLink22 in self.links:
							continue

						# add new links
						switches[i].addLink(torLink11)
						switches[index1].addLink(torLink11)
						switches[i].addLink(torLink21)
						switches[index2].addLink(torLink21)

						# remove links
						index1 = -1
						index2 = -2
						for i in range(N):
							if switches[i] == rLink.getDownSwitch():
								index1 = i
							if switches[i] == rLink.getUpSwitch():
								index2 = i
						switches[index1].removeLink(rLink)
						switches[index2].removeLink(rLink)
						self.links.remove(rLink)

						openPorts[i] -= 2
						break

		for server in servers:
			self.devices.append(server)
		for switch in switches:
			self.devices.append(switch)

