import os

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input'), 'r') as f:
    lines = [line.strip() for line in f]

def is_symbol(c):
    return c != '.' and not c.isdigit()

def is_adjust(arr, x, y):
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            try:
                c = arr[x+i][y+j]
            except:
                continue
            if is_symbol(c):
                return True


def easy(lines):
    ret = 0
    nc, nr = len(lines[0]), len(lines)
    for i in range(nr):
        in_number = False
        numbers = ""
        part=False
        for j in range(nc):
            c = lines[i][j]
            if c.isdigit():
                in_number =True
                numbers += c
                if is_adjust(lines, i,j):
                    part=True

            if j==nc-1 or not lines[i][j+1].isdigit():
                if part:
                    ret += int(numbers)
                in_number =False
                part = False
                numbers = ""

    print(ret)
        
def find_gears(arr, x, y):
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            try:
                c = arr[x+i][y+j]
            except:
                continue
            if c == '*':
                yield x+i, y+j

def hard(lines):
    ret = 0
    gears = {}
    nc, nr = len(lines[0]), len(lines)
    for i in range(nr):
        in_number = False
        s = 0
        seen = set()
        for j in range(nc):
            c = lines[i][j]
            if c.isdigit():
                if not in_number:
                    s = j
                    in_number = True
                for x,y in find_gears(lines, i, j):
                    seen.add((x,y))
                 
            if j == nc-1 or not lines[i][j+1].isdigit():
                if not in_number:
                    continue
                in_number = False
                for p in seen:
                    gears.setdefault(p, []).append(int(lines[i][s:j+1]))
                seen = set()

    for gear in gears.values():
        if len(gear) == 2:
            ret += gear[0]*gear[1]

    print(ret)

if __name__ == '__main__':
    tests = '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..'''
    test_lines=tests.split()
    easy(test_lines)
    hard(test_lines)
    easy(lines)
    hard(lines)
