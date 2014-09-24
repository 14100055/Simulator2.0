#import sys, os.path
#sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from base.device import Device
from base.link import Link
from base.event import *

import math
import random

def assignFailures(components):
	component = components[0].getType()
	types = ['tor', 'aggr', 'core']
	resiliences = [0.039, 0.07, 0.02]
	num = len(types)

	comps = []
	for i in range(num):
		ty = types[i]
		if component == 'link':
			ty = ty + 'Link'
		devs = getComponentSpecial(components, ty)
		if len(devs) > 0:
			devs = failureModel(devs, resiliences[i])
			for dev in devs:
				comps.append(dev)
		else:
			print 'No devices'
	return comps


def getComponentSpecial(components, ty):
	comps = []
	for comp in components:
		if comp.getLabel() == ty:
			comps.append(comp)
	return comps


def failureModel(components, resilience):
	num = len(components)
	a_size = num*(1.0-resilience)
	b_size = math.ceil(num*(resilience/2.0))
	c_size = math.ceil(num*(resilience/2.0))

	while c_size:
		component = random.choice(components)
		if component.getFailure() > -1:
			continue
		component.setFailure(2)
		c_size = c_size - 1
	while b_size:
		component = random.choice(components)
		if component.getFailure() > -1:
			continue
		component.setFailure(1)
		b_size = b_size - 1
	for component in components:
		if component.getFailure() > -1:
			continue
		component.setFailure(0)
	return components


def calcFailure(component, id, totalTime):
	if component.getFailure() < 1:
		return None
	componentType = component.getType()
	time = random.randrange(totalTime)
	ev = FailureEvent(id, time, 'Failure', componentType, component)
	return ev


def getTTR(componentType, component):
	val = random.randrange(100)
	if componentType == 'device':
		if component.getLabel() == 'tor':
			return getTTR_ToR(val)
		if component.getLabel() == 'aggr':
			return getTTR_Aggr(val)
		if component.getLabel() == 'core':
			return getTTR_Core(val)
	elif componentType == 'link':
		return getTTR_Link(val)
	return -1


def getTTF(componentType, component):
	val = random.randrange(100)
	if componentType == 'device':
		if component.getLabel() == 'tor':
			return getTTF_ToR(val)
		if component.getLabel() == 'aggr':
			return getTTF_Aggr(val)
		if component.getLabel() == 'core':
			return getTTF_Core(val)
	elif componentType == 'link':
		if component.getLabel() == 'torLink' or component.getLabel() == 'aggrLink':
			return getTTF_PodLink(val)
		if component.getLabel() == 'coreLink':
			return getTTF_CoreLink(val)
	return -1


###########################################################
####### Helper functions to get the time-to-failure #######
###########################################################
def getTTF_ToR(val):
	if val < 8:
		return random.randrange(5, 5*60)
	elif val < 20:
		return random.randrange(5*60, 1000)
	elif val < 40:
		return random.randrange(1000, 60*60)
	elif val < 50:
		return random.randrange(60*60, 17782)
	elif val < 60:
		return random.randrange(17782, 24*60*60)
	elif val < 70:
		return random.randrange(24*60*60, 316227)
	elif val < 80:
		return random.randrange(316227, 7*24*60*60)
	elif val < 90:
		return random.randrange(7*24*60*60, 1995262)
	elif val < 100:
		return random.randrange(1995262, 10000000)

def getTTF_Aggr(val):
	if val < 2:
		return random.randrange(5, 100)
	elif val < 30:
		return random.randrange(100, 5*60)
	elif val < 40:
		return random.randrange(5*60, 60*60)
	elif val < 65:
		return random.randrange(60*60, 24*60*60)
	elif val < 82:
		return random.randrange(24*60*60, 7*24*60*60)
	elif val < 100:
		return random.randrange(7*24*60*60, 3162277)

def getTTF_Core(val):
	if val < 2:
		return random.randrange(5, 100)
	elif val < 45:
		return random.randrange(100, 1000)
	elif val < 70:
		return random.randrange(1000, 60*60)
	elif val < 100:
		return random.randrange(60*60, 10000000)

def getTTF_PodLink(val):
	if val < 20:
		return random.randrange(100, 5*60)
	elif val < 40:
		return random.randrange(5*60, 1000)
	elif val < 60:
		return random.randrange(1000, 60*60)
	elif val < 70:
		return random.randrange(60*60, 50118)
	elif val < 82:
		return random.randrange(50118, 7*24*60*60)
	elif val < 91:
		return random.randrange(7*24*60*60, 1995262)
	elif val < 100:
		return random.randrange(1995262, 7000000)

def getTTF_CoreLink(val):
	if val < 20:
		return random.randrange(100, 5*60)
	elif val < 40:
		return random.randrange(5*60, 60*60)
	elif val < 63:
		return random.randrange(60*60, 24*60*60)
	elif val < 67:
		return random.randrange(24*60*60, 7*24*60*60)
	elif val < 80:
		return random.randrange(7*24*60*60, 1000000)
	elif val < 90:
		return random.randrange(1000000, 3162277)
	elif val < 100:
		return random.randrange(3162277, 10000000)

###########################################################
####### Helper functions to get the time-to-recover #######
###########################################################
def getTTR_ToR(val):
	if val < 40:
		return random.randrange(100, 5*60)
	elif val < 50:
		return random.randrange(5*60, 20*60)
	elif val < 80:
		return random.randrange(20*60, 60*60)
	elif val < 90:
		return random.randrange(60*60, 10000)
	elif val < 98:
		return random.randrange(10000, 24*60*60)
	elif val < 100:
		return random.randrange(24*60*60, 7*24*60*60)

def getTTR_Aggr(val):
	if val < 20:
		return random.randrange(100, 5*60)
	elif val < 80:
		return random.randrange(5*60, 562)
	elif val < 90:
		return random.randrange(562, 1000)
	elif val < 97:
		return random.randrange(1000, 60*60)
	elif val < 100:
		return random.randrange(60*60, 10000)

def getTTR_Core(val):
	if val < 50:
		return random.randrange(100, 5*60)
	elif val < 70:
		return random.randrange(5*60, 1000)
	elif val < 100:
		return random.randrange(1000, 7*24*60*60)

def getTTR_Link(val):
	if val < 20:
		return random.randrange(100, 171)
	elif val < 40:
		return random.randrange(171, 251)
	elif val < 60:
		return random.randrange(251, 5*60)
	elif val < 80:
		return random.randrange(5*60, 400)
	elif val < 90:
		return random.randrange(400, 1000)
	elif val < 95:
		return random.randrange(1000, 60*60)
	elif val < 98:
		return random.randrange(60*60, 24*60*60)
	elif val < 100:
		return random.randrange(24*60*60, 7*24*60*60)