from pathlib import Path

'''
Initial function (hike) created a dictionary of segments that could be referenced once visted.
DFS. Correct approach but tooooo slow. A cyclic graph, as apposed to a DAG (directional acyclic graph),
for longest path problems is considered a NP-Hard problem. There is not a known solution in polynomial time :')
Solving this problem requires optimizations to execute within a reasonable timeframe. 
AOC reddit suggested first using a BFS to build a graph where the intersections are vertice and the paths 
between them are the edges, with weights corresponding to their lengths. 
This was similar to my original approach of storing all the paths in a dict.
Once the graph was created, a second DFS function created an exhaustive list of paths to find the longest.
This is still quite slow!!!
'''

data = Path('/Users/benmelodics/Desktop/AdventOfCode/23/day-23-input-1.txt').read_text().splitlines()
l = len(data)
edges = (-1, l)

def bfs_graph_hike(data):

	start, end = (0,1), (l-1,l-2)
	path_queque = [[[start], (0,1)]]
	segments = {(0,1):{}}
	visited = []

	while len(path_queque) > 0:

		current_path, origin = path_queque[0]
		p = current_path[-1]
		segment_start = current_path[0]

		directions = [(p[0]-1, p[1]), (p[0], p[1]-1),(p[0]+1, p[1]), (p[0], p[1]+1)]
		valid_moves = []

		for d in directions:

			if d in segments.keys() and d != origin:
				segments[origin][d] = len(current_path) + 1
				segments[d][origin] = len(current_path) + 1

			elif d[0] not in edges and d[1] not in edges and d not in visited:
				if data[d[0]][d[1]] != '#':
					valid_moves.append(d)
				else:
					pass

		if len(valid_moves) == 0:
			if p == end:
				segments[origin][p] = len(current_path) - 1
				segments[p] = {origin:len(current_path)}
			del path_queque[0]

		elif len(valid_moves) > 1:
			segments[origin][p] = len(current_path) 
			segments[p] = {origin:len(current_path)}
			for move in valid_moves:
				path_queque.append([[move], p])
			del path_queque[0]

		else:
			current_path.append(valid_moves[0])

		visited.append(p)

	return segments

def dfs(graph):

	end = (l-1,l-2)
	stack = [([(0,1)], 0)]
	completed_paths = []

	while len(stack) > 0:

		path_data = stack[-1]
		path, length = path_data
		pos = path[-1]
		nodes = graph[pos]

		if pos == end:
			completed_paths.append(length)

		del stack[-1]

		for n in nodes.keys():
			if n not in path:
				stack.append((path + [n], length + nodes[n]))

	return completed_paths, max(completed_paths)

def hike(data):

	start, end = (0,1), (l-1,l-2)
	path_stack = [[[start], start]]
	completed_paths = [1]
	segments = {}

	while len(path_stack) > 0:

		lp = path_stack[-1]
		p = lp[0][-1]
		current_path = lp[0]
		segment_start = lp[1]
		up, left, down, right = [(p[0]-1, p[1]), (p[0], p[1]-1),( p[0]+1, p[1]), (p[0], p[1]+1)]
		directions = [up, left, down, right]
		valid_moves = []

		if p == end:
			completed_paths.append(len(current_path)-1)
			print(max(completed_paths))
			del path_stack[-1]

		else:
			for d in directions:
				if d != (-1, 1) and d not in current_path:
					tile = data[d[0]][d[1]]
					if tile != '#':
						valid_moves.append(d)
					else:
						pass

			if len(valid_moves) == 0:
				if segment_start not in segments.keys():
					segments[segment_start] = current_path[current_path.index(segment_start):]
				del path_stack[-1]

			elif len(valid_moves) > 1:
				if segment_start not in segments.keys():
					segments[segment_start] = current_path[current_path.index(segment_start):]

				del path_stack[-1]

				for move in valid_moves:
					if move in segments.keys():
						path_stack.append([current_path + segments[move], move])
					else:
						path_stack.append([current_path + [move], move])
			else:
				current_path.append(valid_moves[0])

	return max(completed_paths)


hike_data = bfs_graph_hike(data)
print(dfs(hike_data))




