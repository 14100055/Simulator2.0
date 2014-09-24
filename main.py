from topology.topology import Topology
import base.handler as handle
import failure.failure as fail

import random
import time

def main():
	random.seed(None)
	eventID = 0
	# generating topology
	topology_type = raw_input("Enter the type of topology to create: ")
	if topology_type == "FatTree" or topology_type == "f":
		attributes = []
		attributes.append(int(raw_input("Enter value of k: ")))
		topology = Topology("FatTree", attributes)
	elif topology_type == "JellyFish" or topology_type == "j":
		attributes = []
		attributes.append(int(raw_input("Enter value of N: ")))
		attributes.append(int(raw_input("Enter value of k: ")))
		attributes.append(int(raw_input("Enter value of r: ")))
		attributes.append(int(raw_input("Enter value of s: ")))
		topology = Topology("JellyFish", attributes)
	else:
		print "Not a valid type of topology. Exiting..."
		return

	print 'Generated topology!'
	try:
		time = int(raw_input("Simulation time (in sec): "))
	except:
		print 'Invalid input! Please try again. Exiting...'
		return

	# generating pre-computed failures based on failure model
	events = []	
	numEvents = 0

	# assign number of failures to devices
	devices = topology.getDevices()
	devices = fail.assignFailures(devices)
	# then create failure event for devices
	for device in devices:
		ev = fail.calcFailure(device, eventID, time)
		if ev is None:
			continue

		device.setFailure(-1)
		evTime = ev.getEventTime()
		inserted = False
		for n in range(numEvents):
			if events[n].getEventTime() > evTime:
				events.insert(n, ev)
				inserted = True
				break
		if not inserted:
			events.append(ev)
		numEvents = numEvents + 1
		eventID = eventID + 1

	print 'Number of events: ' + str(numEvents)

	# assign number of failures to links
	links = topology.getLinks()
	links = fail.assignFailures(links)
	# then create failure event for links
	for link in links:
		ev = fail.calcFailure(link, eventID, time)
		if ev == None:
			continue

		link.setFailure(-1)
		evTime = ev.getEventTime()
		inserted = False
		for n in range(numEvents):
			if events[n].getEventTime() > evTime:
				events.insert(n, ev)
				inserted = True
				break
		if not inserted:
			events.append(ev)
		numEvents = numEvents + 1
		eventID = eventID + 1

	print 'Number of events: ' + str(numEvents)

	print 'Starting simulation!'
	nextEventTime = events[0].getEventTime()
	# main loop to iterate through "time"
	for i in range(time):
		if i % 1000 == 0:
			print 'Run: ' + str(i)

		while i == nextEventTime:
			ev = handle.handleEvent(events[0], topology, eventID)
			events = events[1:]
			numEvents = numEvents - 1
			if ev is not None:
				evTime = ev.getEventTime()
				inserted = False
				for n in range(numEvents):
					if events[n].getEventTime() > evTime:
						events.insert(n, ev)
						numEvents = numEvents + 1
						eventID = eventID + 1
						inserted = True
						break
				if not inserted:
					events.append(ev)
			try:
				# the general case
				nextEventTime = events[0].getEventTime()
			except:
				# in case there are no more events
				nextEventTime = -1

	print 'Completed simulation!'
	print 'Calling a function to print or write to file all the metrics/statistics'


if __name__ == '__main__':
	main()