from pathlib import Path
from itertools import combinations
from random import randint
import copy

'''
Mininum Cut Problem - https://en.wikipedia.org/wiki/Minimum_cut

Solved using Kargers algorithm which uses monte carlo, random sampling to reduce the number of 
super vertices down to two. Given the vertices we are searching for will naturally have a low number of edges,
there is a high enough probability that the algorithm will produce the correct result within a 
reasonable number of attempts. 

The randomness means the run time can vary quite a bit. This example took about a minute to produce the correct
result, runnning the algorithm 36 times.

test_connections and generate_connections are redundant functions.

Initally I created modeled testing a circuit, starting with side a of the module
and seeing if side b was reached. Trying this for every combination of 3 missing wires 
was obviously not scalable :,(
'''


data = Path('/Users/benmelodics/Desktop/AdventOfCode/23/day-25-input-1.txt').read_text().splitlines()
l = len(data)

def snowverload(data):

	components = {}

	for row in data:

		comp, con = row.split(':')
		con = con.split()

		if comp in components.keys():
			for c in con:
				if c not in components[comp]:
					components[comp].add(c)
		else:
			components[comp] = set(con)

		for c in con:
			if c in components.keys():
				if comp not in components[c]:
					components[c].add(comp)
			else:
				components[c] = {comp}

	components = {k:list(components[k]) for k in components.keys()}
	components_ = {}

	for k in components.keys():
		components_[k] = []
		for v in components[k]:
			v = [k, v]
			v.sort()
			v = '-'.join(v)
			components_[k].append(v)

	return components_


def test_connections(connection, components, l):

	a, b = connection[0]
	c, d = connection[1]
	e, f = connection[2]
	connection_list = [[a, b], [b, a], [c, d], [d, c], [e, f], [f, e]]

	visited_a = []
	queque = [a]

	while len(queque) > 0:
		k = queque[0]
		if visited_a == l: 
			break
		for c in components[k]:
			if c not in visited_a and c not in queque and [k, c] not in connection_list:
				queque.append(c)
		visited_a.append(k)
		queque.pop(0)

	visited_b = []
	queque = [b]

	if len(visited_a) != l:

		while len(queque) > 0:
			k = queque[0]
			for c in components[k]:
				if c not in visited_b and c not in queque and [k, c] not in connection_list:
					queque.append(c)
			visited_b.append(k)
			queque.pop(0)

	else:
		return l, l, l

	return len(set(visited_a).intersection(set(visited_b))), sum([len(visited_a), len(visited_b)]), len(visited_a) * len(visited_b)


def generate_connections(components):

	single_connections = []

	for k in components.keys():
		for c in components[k]:
			if len(components[k].intersection(components[c])) < 1:
				if [k, c] not in single_connections and [c, k] not in single_connections:
					single_connections.append([k, c])

	comb = combinations(single_connections, 3)
	co_ = 0
	l = len([k for k in components.keys()])
	print('l: ', l)

	for co in comb:
		test_connections(co, components, l)


def kargers(components):

	kagers_list = []

	for x in range(100):

		c = copy.deepcopy(components)

		while len(c.keys()) > 2:

			vertice = [x for x in c.keys()][randint(0, len(c.keys())-1)]
			edge = c[vertice][randint(0, len(c[vertice])-1)]

			second_vertice = ''
			for k in c.keys():
				for l in c[k]:
					if k != vertice and l == edge:
						second_vertices = k

			new_vertice = str(vertice) + '_' + str(second_vertices)

			c[new_vertice] = list(set(c[vertice] + c[second_vertices]))

			super_key = new_vertice.split('_')

			cleaned_edges = []

			for e in c[new_vertice]:
				e_sp = e.split('-')
				if e_sp[0] not in super_key or e_sp[1] not in super_key:
					cleaned_edges.append(e)

			c[new_vertice] = cleaned_edges

			del c[vertice]
			del c[second_vertices]

		if len(c[new_vertice]) == 3:
			output = [len(x.split('_')) for x in c.keys()] 
			return x, c, output[0] * output[1]


print(kargers(snowverload(data)))