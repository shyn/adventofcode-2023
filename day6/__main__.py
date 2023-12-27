def parse(f):
    lines = [line.split(':')[1].strip().split() for line in f]
    for t, d in zip(*lines):
        yield int(t), int(d)
    

def part1(f):
    # (t - n)*n > d
    ret = 1
    for t, d in parse(f):
        count = 0
        for i in range(1, t):
            if (t - i)*i > d:
                count += 1
        ret *= count
    print(ret)


def part2(f):
    t, d = [int(line.split(':')[1].strip().replace(' ', '')) for line in f]
    l, r = 0, t
    while (t-l)*l <= d:
        l += 1
    while (t-r)*r <= d:
        r -= 1

    print(r-l+1)



if __name__ == '__main__':
    test_lines='''Time:      7  15   30
Distance:  9  40  200'''
    part1(test_lines.split('\n'))
    input='''Time:        45     97     72     95
Distance:   305   1062   1110   1695'''
    part1(input.split('\n'))

    part2(test_lines.split('\n'))
    part2(input.split('\n'))
