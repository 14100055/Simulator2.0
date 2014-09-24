import sys, os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import failure.failure as fail
from base.event import *

def handleEvent(event, topology, lastID):
	evType = event.getEventType()
	
	if evType == 'Failure':
		return handleFailure(event, topology, lastID)
	elif evType == 'Recovery':
		return handleRecovery(event, topology, lastID)
	elif evType == 'TenantArrival':
		return handleTenantArrival(event, topology)
	elif evType == 'FlowArrival':
		return handleFlowArrival(event, topology)
	return None


def handleFailure(event, topology, lastID):
	# print str(event.getEventTime()) + ') Handling failure'
	componentType = event.getComponentType()
	component = event.getComponent()
	component.toggleStatus()

	ttR = fail.getTTR(componentType, component)
	if ttR == -1:
		return None

	id = lastID + 1
	time = event.getEventTime() + ttR
	ev = RecoveryEvent(id, time, 'Recovery', componentType, component)
	return ev


def handleRecovery(event, topology, lastID):
	# print str(event.getEventTime()) + ') Handling recovery'
	componentType = event.getComponentType()
	component = event.getComponent()
	component.toggleStatus()
	if component.getFailure() == 0:
		return None
	component.setFailure(-1)

	ttF = fail.getTTF(componentType, component)
	if ttF == -1:
		return None

	id = lastID + 1
	time = event.getEventTime() + ttF
	ev = FailureEvent(id, time, 'Failure', componentType, component)
	return ev


def handleTenantArrival(event, topology):
	print 'Handling tenant arrival'
	return None

def handleFlowArrival(event, topology):
	print 'Handling flow arrival'
	return None