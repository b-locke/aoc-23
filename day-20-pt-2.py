from pathlib import Path
from collections import OrderedDict
import math

''' 
Assumed it was something to do with finding the LCM but was unsure of the inputs, had to consult reddit.
The final conjunction module has four inputs, each of which is a conjunction module. These modules are
all on different cycles. By finding the lowest number of button presses it takes for each module to send a high pulse, we
can calculate the LCM as the point at which they are in phase.
'''

data = Path('/Users/benmelodics/Desktop/AdventOfCode/23/day-20-input-1.txt').read_text().splitlines()

broadcast_dict = {'out':[]}
modules = {}
button = 'low'
conjunction_inputs = []

for line in data:

	i, o = [x.strip() for x in line.split('->')]
	if ',' in o:
		o = [x.strip() for x in o.split(',')]
	else:
		o = [o]

	if i == 'broadcaster':
		broadcast_dict['out'] = o

	elif i[0] == '%':
		modules[i[1:]] = {'type': '%', 'state': 'off', 'out':o}

	elif i[0] == '&':
		modules[i[1:]] = {'type': '&', 'in': {}, 'out':o}

for line in data:

	i, o = [x.strip() for x in line.split('->')]
	if ',' in o:
		o = [x.strip() for x in o.split(',')]
	else:
		o = [o]

	for x in o:
		if x in modules.keys():
			if modules[x]['type'] == '&':
				modules[x]['in'][i[1:]] = 'low'

def broadcast(pulse):
	for x in broadcast_dict['out']:
		sequence.append((x, pulse, 'broadcast'))
	sequence.pop(0)

def flip_flop(mod, pulse):
	if pulse == 'low':
		if modules[mod]['state'] == 'off':
			modules[mod]['state'] = 'on'
			for x in modules[mod]['out']:
				sequence.append((x, 'high', mod))
		else:
			modules[mod]['state'] = 'off'
			for x in modules[mod]['out']:
				sequence.append((x, 'low', mod))
	sequence.pop(0)

def conjunction(mod, pulse, sender, count):
	modules[mod]['in'][sender] = pulse
	if mod == 'vr' and pulse == 'high':
		if sender not in vr_hp.keys():
			vr_hp[sender] = count

	for x in modules[mod]['out']:
		if 'low' not in modules[mod]['in'].values():
			sequence.append((x, 'low', mod))
		else:
			sequence.append((x, 'high', mod))
	sequence.pop(0)	

def pulse(count):
	rx_count = 0
	while len(sequence) > 0:
		mod, pulse, sender = sequence[0]
		if mod == 'broadcast':
			gpc[pulse] += 1
			broadcast(pulse)

		elif mod not in modules.keys():
			rx_count += 1
			gpc[pulse] += 1
			sequence.pop(0)

		else:
			mod_type = modules[mod]['type']
			if mod_type == '%':
				gpc[pulse] += 1
				flip_flop(mod, pulse)
			else:
				gpc[pulse] += 1
				conjunction(mod, pulse, sender, count)
	return rx_count


#print(modules, '\n')
sequence = [('broadcast', 'low', 'button')]
gpc = {'high':0, 'low':0}
vr_hp = {}
count = 1

while len(vr_hp.keys()) < 4:
	sequence = [('broadcast', 'low', 'button')]
	rx_count = pulse(count)	
	count+=1

vr_l = [x for x in vr_hp.values()]

print(math.lcm(vr_l[0], vr_l[1], vr_l[2], vr_l[3]))
#print(gpc['high']*gpc['low'])

