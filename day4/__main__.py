import os

with open(os.path.join(os.path.realpath(os.path.dirname(__file__)), 'input'), 'r') as f:
    lines = [line.strip() for line in f]

def part1(lines):
    ret = 0
    for line in lines:
        _, main_part = line.split(':')
        winning_part, guess_part = main_part.split('|')
        winning_numbers = winning_part.strip().split()
        guess_numbers = guess_part.strip().split()
        i = 0
        point = 0
        for n in guess_numbers:
            if n in winning_numbers:
                point = 2**i
                i +=1
        ret += point
    print(ret)

def part2(lines):
    ret = 0
    score = [1]*len(lines)
    for row, line in enumerate(lines):
        _, main_part = line.split(':')
        winning_part, guess_part = main_part.split('|')
        winning_numbers = winning_part.strip().split()
        guess_numbers = guess_part.strip().split()
        i = 0
        for n in guess_numbers:
            if n in winning_numbers:
                i +=1
        for j in range(row+1, row+i+1):
            score[j] += score[row]
    print(sum(score))


if __name__ == '__main__':
    tests='''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'''
    test_lines = [line.strip() for line in tests.split('\n')]
    part1(test_lines)
    part1(lines)
    part2(test_lines)
    part2(lines)
