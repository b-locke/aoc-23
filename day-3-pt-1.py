import pathlib

puzzle_input = pathlib.Path('/Users/benjamin/Documents/GitHub/aoc-23/day-3-input-1.txt').read_text().splitlines()
#puzzle_input = puzzle_input[:4]

def symbol_locations(puzzle_input):
    ### Find all symbol rows and columns, storing them in a list of tuples.
    symbol_location_list = []
    for row in range(len(puzzle_input)):
    	for col in range(len(puzzle_input[row])):
    		position = puzzle_input[row][col]
    		if position.isnumeric() == False and position != '.':
    			symbol_location_list.append((row, col))
    return symbol_location_list


def number_locations(puzzle_input, symbol_locations_data):
	### Find all part numbers and compare their location to the symbols locations.
	valid_parts = []
	active_number = []
	active_number_valid = False

	for row in range(len(puzzle_input)):
		for col in range(len(puzzle_input[row])):

			position = puzzle_input[row][col]

			### Check if position is not numeric and append value to part list if it's a valid part
			if position.isnumeric() == False and active_number_valid == True:
				valid_parts.append(active_number)
				active_number_valid = False
				active_number = []

			elif position.isnumeric() == False and active_number_valid == False:
				active_number_valid = False
				active_number = []
			
			else:
				### If the position is numeric, test validity
				active_number.append(position)
				adjacents = [(row-1, col), (row, col+1), (row+1, col), (row, col-1), (row-1, col-1), (row-1, col+1), (row+1, col-1), (row+1, col+1)]
				adjacents_found = [True for p in adjacents if p in symbol_locations_data]

				if True in adjacents_found:
					active_number_valid = True

	return [int(''.join(part)) for part in valid_parts if len(part) > 0]

symbol_locations_data = symbol_locations(puzzle_input)
valid_parts = number_locations(puzzle_input, symbol_locations_data)
print(sum(valid_parts))
