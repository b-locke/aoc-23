from pathlib import Path

data_ = Path('/Users/benmelodics/Desktop/AdventOfCode/23/day-21-input-1.txt').read_text().splitlines()
l = len(data_)
print(l)
start = [(r, c) for c in range(l) for r in range(l) if data_[r][c] == 'S'][0]

### Make a 5 x 5 grid

x7_grid = [c*7 for c in data_]*7
lx7 = len(x7_grid)
start = (int(lx7*0.5), int(lx7*0.5))
edges = [-1, lx7+1]

def step_counter(data, start):

	visited_plots = {}
	visiting_plots = [start]
	unvisited_plots = []
	quardratic_points = {64:'', 65:'', 196:'', 327:''}

	for step in range(0, (65+(2*131))+1):
		#print(step)
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

		if step in quardratic_points.keys():
			if step % 2 == 0:
				quardratic_points[step] = len([k for k in visited_plots.keys() if visited_plots[k] % 2 == 0])
			else:
				quardratic_points[step] = len([k for k in visited_plots.keys() if visited_plots[k] % 2 != 0])


	even_steps = len([k for k in visited_plots.keys() if visited_plots[k] % 2 == 0])

	c = quardratic_points[65]
	b = (4*quardratic_points[196] - 3*quardratic_points[65] - quardratic_points[327])//2
	a = quardratic_points[196] - quardratic_points[65] - b

	x = (26501365 - 65)//l 

	p = a*(x**2) + b*x + c

	return p

print(step_counter(x7_grid, start))


