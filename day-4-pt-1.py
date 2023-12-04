import pathlib
from functools import reduce

puzzle_input = pathlib.Path('/Users/benjamin/Documents/GitHub/aoc-23/day-4-input-test.txt').read_text().splitlines()

def scratchcard_scores(puzzle_input):
	total_points = 0
	for line in puzzle_input:
		card_number = 1
		winning_numbers, numbers_you_have = line.split(':')[1].split('|')
		winning_numbers = [int(num) for num in winning_numbers.split()]
		numbers_you_have = [int(num) for num in numbers_you_have.split()]
		correct_nums = 0
		for n in numbers_you_have:
			if n in winning_numbers:
				correct_nums += 1
		card_points = 2 ** (correct_nums - 1) if correct_nums > 1 else correct_nums
		total_points += card_points
		print(card_points)

	return total_points


output = scratchcard_scores(puzzle_input)
print(output)
