from pathlib import Path

### Very slow during the collapsing stage, takes a few minutes to run...

data = Path('/Users/benmelodics/Desktop/AdventOfCode/23/day-22-input-1.txt').read_text().splitlines()
s = {i : {'start': [int(n) for n in x.split('~')[0].split(',')], 'end': [int(n) for n in x.split('~')[1].split(',')], 'dependencies':[], 'connections':[], 'supported_by':[]} for i, x in enumerate(data)}
sorted_s = {}

z_start = sorted([s[z]['start'][2] for z in s.keys()])
for i, z in enumerate(z_start):
	for k in s.keys():
		if s[k]['start'][2] == z:
			sorted_s[i] = s[k]
			del s[k]
			break
s = sorted_s

xl = max([max(s[x]['start'][0], s[x]['end'][0]) for x in s.keys()])
yl = max([max(s[x]['start'][1], s[x]['end'][1]) for x in s.keys()])
zl = max([max(s[x]['start'][2], s[x]['end'][2]) for x in s.keys()])

grid = [[['.'for x in range(xl+1)] for y in range(yl+1)] for z in range(zl+1)]

disintegration = [sk for sk in s.keys()]
preservation = []

for k in s.keys():
	s_x, s_y, s_z = s[k]['start']
	e_x, e_y, e_z = s[k]['end']
	x_r = [i for i in range(s_x, e_x+1)]
	y_r = [i for i in range(s_y, e_y+1)]
	z_r = [i for i in range(s_z, e_z+1)]
	positions = [[x, y, z] for x in x_r for y in y_r for z in z_r]
	pos_single_layer = [[x, y, z] for x in x_r for y in y_r for z in [min(z_r)]]
	settled = False
	clear = True
	z_offset = 1
	supporting_bricks = []

	while settled == False:

		for p in pos_single_layer:
			if p[2] - z_offset == 0:
				for i in positions:
					grid[i[2] - z_offset+1][i[1]][i[0]] = k
				settled = True

			elif grid[p[2] - z_offset][p[1]][p[0]] != '.':
				clear = False
				g = grid[p[2] - z_offset][p[1]][p[0]]
				if g not in supporting_bricks:
					supporting_bricks.append(g)
					s[k]['supported_by'].append(g)

		if clear == False:
			for i in positions:
				grid[i[2] - z_offset+1][i[1]][i[0]] = k

			if len(supporting_bricks) == 1:
				s[supporting_bricks[0]]['dependencies'].append(k)
				s[supporting_bricks[0]]['connections'].append(k)
			else:
				for support in supporting_bricks:
					s[support]['connections'].append(k)

			settled = True

		z_offset+=1

collapse_count = 0
for k in s.keys():
	collapse_list = []
	if len(s[k]['dependencies']) > 0:
		for d in s[k]['dependencies']:
			collapse = [d]
			collapse_list.append(d)
			while len(collapse) > 0:
				collapsing_brick = collapse[0]
				for c in s[collapsing_brick]['connections']:
					all_supports_missing = True
					for supports in s[c]['supported_by']:
						if supports not in collapse_list:
							all_supports_missing = False
					if all_supports_missing == True:
						collapse.append(c)
						if c not in collapse_list:
							collapse_list.append(c)
				collapse.pop(0)
	collapse_count += len(set(collapse_list))

print(collapse_count)




