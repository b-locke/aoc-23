import pathlib

puzzle_input = pathlib.Path('/Users/benjamin/Documents/GitHub/aoc-23/day-1-input-1.txt').read_text().splitlines()

def parse(puzzle_input):

	output_list = []
	value_dict = {'left': '', 'right': ''}

	for line in puzzle_input:
		i = 0
		l = len(line) - 1

		while value_dict['left'] == '':
			if line[i].isnumeric():
				value_dict['left'] = line[i]
			i += 1

		while value_dict['right'] == '':
			if line[l].isnumeric():
				value_dict['right'] = line[l]
			l -= 1

		output_list.append(int(value_dict['left'] + value_dict['right']))
		value_dict['left'] = ''
		value_dict['right'] = ''

	return sum(output_list)

print(parse(puzzle_input))