from pathlib import Path

data = Path('/Users/benmelodics/Desktop/AdventOfCode/23/day-23-input-1.txt').read_text().splitlines()
l = len(data)
edges = (-1, l)

def hike(data):

	start, end = (0,1), (l-1,l-2)
	visited_paths, current_path, path_queue = {}, [], [[start]]

	while len(path_queue) > 0:

		p = path_queue[0][-1]
		up, down, left, right = [(p[0]-1, p[1]), (p[0]+1, p[1]), (p[0], p[1]-1), (p[0], p[1]+1)]
		directions = [up, down, left, right]
		valid_moves = []
		visited_paths_ends = [visited_paths[v]['end'] for v in visited_paths.keys()]

		for i, d in enumerate(directions):
			if d[0] not in edges and d[1] not in edges and d not in path_queue[0]:
				if len(path_queue[0]) == 1:
					if d not in visited_paths_ends:
						tile = data[d[0]][d[1]]
						if tile != '#':
							if tile != '.':
								if i == 0 and tile == '^':
									valid_moves.append(d)
								elif i == 1 and tile == 'v':
									valid_moves.append(d)
								elif i == 2 and tile == '<':
									valid_moves.append(d)
								elif i == 3 and tile == '>':
									valid_moves.append(d)
							elif tile == '.':
								valid_moves.append(d)
							else:
								pass

				else:
					tile = data[d[0]][d[1]]
					if tile != '#':
						if tile != '.':
							if i == 0 and tile == '^':
								valid_moves.append(d)
							elif i == 1 and tile == 'v':
								valid_moves.append(d)
							elif i == 2 and tile == '<':
								valid_moves.append(d)
							elif i == 3 and tile == '>':
								valid_moves.append(d)
						elif tile == '.':
							valid_moves.append(d)
						else:
							pass

		if len(valid_moves) == 0:
			visited_paths[len(visited_paths.keys())] = {'path': path_queue[0], 'length': len(path_queue[0]), 'start': path_queue[0][0], 'end': path_queue[0][-1], 'connections':[]}
			path_queue.pop(0)

		elif len(valid_moves) > 1:
			for move in valid_moves:
				path_queue.append([move])
			visited_paths[len(visited_paths.keys())] = {'path': path_queue[0], 'length': len(path_queue[0]), 'start': path_queue[0][0], 'end': path_queue[0][-1], 'connections':valid_moves}
			path_queue.pop(0)

		else:
			path_queue[0].append(valid_moves[0])

	return visited_paths

def hike_lengths(hike_data):

	joined_paths = [[hike_data[0]['start']]]

	for path in hike_data.keys():
		new_paths = []
		for j in joined_paths:
			if j[-1] == hike_data[path]['start']:
				for c in hike_data[path]['connections']:
					new_paths.append(j + [c])
				if len(hike_data[path]['connections']) > 0:
					joined_paths.remove(j)
		joined_paths += new_paths


	path_lengths = []

	for path in joined_paths:
		path_length = 0
		for node in path:
			for k in hike_data.keys():
				if hike_data[k]['start'] == node:
					path_length += hike_data[k]['length']
					break
		path_lengths.append(path_length-1)


	return(path_lengths)

hike_data = hike(data)
print(hike_lengths(hike_data))
