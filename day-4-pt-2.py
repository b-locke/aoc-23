import pathlib
from functools import reduce

puzzle_input = pathlib.Path('/Users/benjamin/Documents/GitHub/aoc-23/day-4-input-1.txt').read_text().splitlines()

def scratchcard_scores(puzzle_input):
	
	total_cards = 0
	cards = {card : 1 for card in range(1, len(puzzle_input) + 1)}

	for line in puzzle_input:

		card_number = int(line.split(':')[0].split()[1])
		winning_numbers, numbers_you_have = line.split(':')[1].split('|')
		winning_numbers = [int(num) for num in winning_numbers.split()]
		numbers_you_have = [int(num) for num in numbers_you_have.split()]

		total_cards += cards[card_number]

		### Caluculate the points for that card
		correct_nums = 0
		for n in numbers_you_have:
			if n in winning_numbers:
				correct_nums += 1
		card_points = 2 ** (correct_nums - 1) if correct_nums > 1 else correct_nums

		### While there are cards of the current card number
		while cards[card_number] > 0:

			### Update bonus cards dictionary
			for n in range(1, correct_nums + 1):
				cards[card_number + n] += 1

			cards[card_number] -= 1

	return total_cards


output = scratchcard_scores(puzzle_input)
print(output)
