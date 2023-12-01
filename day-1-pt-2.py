import pathlib

puzzle_input = pathlib.Path('/Users/benjamin/Documents/GitHub/aoc-23/day-1-input-1.txt').read_text().splitlines()
def parse(puzzle_input):

	output_list = []
	value_dict = { 'left': '', 'right': '' }
	number_dict = { 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9' }
	number_dict_keys = number_dict.keys()

	for line in puzzle_input:

		value_dict['left'] = ''
		value_dict['right'] = ''

		s = 0

		while value_dict['left'] == '':
			if line[s].isnumeric():
				value_dict['left'] = line[s]
			else:
				for key in number_dict_keys:
					if key in line[:s+1]:
						value_dict['left'] = number_dict[key]
			s += 1


		e = len(line) - 1

		while value_dict['right'] == '':
			if line[e].isnumeric():
				value_dict['right'] = line[e]
			else:
				for key in number_dict_keys:
					if key in line[e:]:
						value_dict['right'] = number_dict[key]
			e -= 1

		output_list.append(int(value_dict['left'] + value_dict['right']))

	return sum(output_list)

print(parse(puzzle_input))