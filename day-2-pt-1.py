import pathlib

puzzle_input = pathlib.Path('/Users/benjamin/Documents/GitHub/aoc-23/day-2-input-1.txt').read_text().splitlines()
#puzzle_input = puzzle_input[:4]
def parse(puzzle_input):

	cube_dict = {'red' : 12, 'green' : 13, 'blue' : 14}
	id_total = 0

	for line in puzzle_input:

		line_games = [games.split(',') for games in line.split(':')[1].split(';')]
		game_id = int(line.split(':')[0].split()[-1])
		number_of_games = len(line_games)
		possible_game = True

		for game in line_games:
			for cubes in game:
				cube_count, cube_colour = cubes.split()
				cube_max = cube_dict[cube_colour]

				#print('game_id: ', game_id, 'cube_count: ', cube_count, 'cube_colour: ', cube_colour, 'cube_max: ', cube_max)

				if int(cube_count) > cube_max:
					possible_game = False

			#print('------------ id_total: ', id_total)

		if possible_game:
			id_total += game_id

	print(id_total)

parse(puzzle_input)
