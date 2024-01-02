from pathlib import Path

data = Path('/Users/benmelodics/Desktop/AdventOfCode/23/day-21-input-1.txt').read_text().splitlines()
l = len(data)
edges = [-1, l]
start = [(r, c) for c in range(l) for r in range(l) if data[r][c] == 'S'][0]

def step_counter(data, start):

	visited_plots = {}
	visiting_plots = [start]
	unvisited_plots = []

	for step in range(0, 65):
		for plot in visiting_plots:
			r = plot[0]
			c = plot[1]
			directions = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]

			for d in directions:
				dr = d[0]
				dc = d[1]
				if dr not in edges and dc not in edges and data[dr][dc] != '#':
					if d not in visited_plots and d not in unvisited_plots:
						unvisited_plots.append(d)

			visited_plots[plot] = step

		visiting_plots = unvisited_plots
		unvisited_plots = []

	even_steps = len([k for k in visited_plots.keys() if visited_plots[k] % 2 == 0])

	return even_steps


print(step_counter(data, start))
