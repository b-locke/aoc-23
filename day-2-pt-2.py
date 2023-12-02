import pathlib

puzzle_input = pathlib.Path('/Users/benjamin/Documents/GitHub/aoc-23/day-2-input-1.txt').read_text().splitlines()
#puzzle_input = puzzle_input[:4]
def parse(puzzle_input):

	power_total = 0

	for line in puzzle_input:

		line_games = [games.split(',') for games in line.split(':')[1].split(';')]
		game_id = int(line.split(':')[0].split()[-1])
		number_of_games = len(line_games)
		possible_game = True
		cube_min_dict = {'red' : 0, 'green' : 0 , 'blue' : 0}

		for game in line_games:
			for cubes in game:
				cube_count, cube_colour = cubes.split()
				if int(cube_count) > cube_min_dict[cube_colour]:
					cube_min_dict[cube_colour] = int(cube_count)

		game_power = cube_min_dict['red'] * cube_min_dict['green'] * cube_min_dict['blue']
		print(game_power)
		power_total += game_power

	print(power_total)

parse(puzzle_input)
