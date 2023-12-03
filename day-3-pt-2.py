import pathlib
from functools import reduce

puzzle_input = pathlib.Path('/Users/benjamin/Documents/GitHub/aoc-23/day-3-input-1.txt').read_text().splitlines()

def number_locations(puzzle_input):
	### Find all part numbers and compare their location to the symbols locations.
	number_location_dict = {}
	active_number = []
	active_number_locations = []
	part_id = 0
	for row in range(len(puzzle_input)):
		for col in range(len(puzzle_input[row])):
			position = puzzle_input[row][col]
			### Check if position is not numeric and append value to part list if it's a valid part
			if position.isnumeric() == False:
				for location in active_number_locations:
					number_location_dict[location] = {'value': int(''.join(active_number)), 'id': part_id}
				active_number_locations	= []
				active_number = []
				part_id += 1	
			else:
				active_number.append(position)
				active_number_locations.append((row, col))
	return number_location_dict

def compare_cog_locations_to_number_locations(puzzle_input, number_location_dict):

    cog_values_list = []
    valid_number_location_keys = number_location_dict.keys()
    for row in range(len(puzzle_input)):
    	for col in range(len(puzzle_input[row])):
    		position = puzzle_input[row][col]
    		if position == '*':
    			### Create a list of parts that surround the cog
    			part_values_list = []
    			part_id_list = []
    			part_location_list = []
    			adjacents = [(row-1, col), (row, col+1), (row+1, col), (row, col-1), (row-1, col-1), (row-1, col+1), (row+1, col-1), (row+1, col+1)]
    			### Use the locations of parts as keys to find their values and add them to the part_values_list
    			for a in adjacents:
    				if a in number_location_dict:
    					if number_location_dict[a]['id'] not in part_id_list:
	    					part_id_list.append(number_location_dict[a]['id'])
	    					part_values_list.append(number_location_dict[a]['value'])
    			### If the number of parts is greater than 1, multiply the values in the list together and add to the cog_values_list
    			if len(part_values_list) > 1:
    				cog_values_list.append(reduce(lambda x, y: x * y, part_values_list))
    return sum(cog_values_list)

number_location_dict = number_locations(puzzle_input)
cog_values = compare_cog_locations_to_number_locations(puzzle_input, number_location_dict)
print(cog_values)
