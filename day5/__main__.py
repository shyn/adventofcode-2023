

def parse(f):
    f = iter(f)
    first_line = next(f)
    seeds = map(int, first_line.split(':')[1].strip().split())

    in_new_map = False
    mapper = []
    rules = []
    for line in f:
        line = line.strip()
        if not line:
            if rules and in_new_map:
                mapper.append(rules)
                rules = []
                in_new_map = False
            continue

        if 'map:' in line:
            in_new_map = True
            continue

        # add rules
        assert len(line.split())==3, line
        rules.append(list(map(int, line.split())))
    if rules:
        mapper.append(rules)

    return seeds, mapper    
   
def part1(f):
    seeds, mapper = parse(f)
    def find_position(seed):
        for rules in mapper:
            for destination, source, n in rules:
                if source <= seed < source+n:
                    seed = destination + seed - source
                    break

        return seed
    
    lowest = min(map(find_position, seeds))
    print(lowest)


def part2(f):
    oseeds, mapper = parse(f)
    def find_position(seed):
        for rules in mapper:
            for destination, source, n in rules:
                if source <= seed < source+n:
                    seed = destination + seed - source
                    break

        return seed
    
    def gen_seeds():
        seeds = list(oseeds)
        pairs = []
        for i in range(0, len(seeds), 2):
            pairs.append((seeds[i], seeds[i]+seeds[i+1]))
        return pairs
    min_in_range = []
    for s, e in gen_seeds():
        seeds = [(s, e)]
        for rules in mapper:
            mapped = []
            for s2, e2 in seeds:
                simple_pairs = [(s2, e2)]
                for dest, source, n in rules:
                    tmp = []
                    for start, end in simple_pairs:
                        if start >= source + n or end < source:
                            tmp.append((start, end))
                            continue
                        # overlap
                        s1 = max(start, source)
                        s2 = min(end, source+n-1)
                        mapped.append((dest+s1-source, dest+s2-source))
                        if start < source:
                            tmp.append((start, source))
                        if end > source+n:
                            tmp.append((source+n, end))
                    simple_pairs = tmp
                mapped.extend(simple_pairs)
            seeds = mapped
        min_in_range.append(min(p[0] for p in seeds))
    print(min(min_in_range))


test_text='''seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4

'''

part1(test_text.split('\n'))
part2(test_text.split('\n'))
import os
with open(os.path.join(os.path.dirname(__file__), 'input'), 'r') as f:
    lines = f.readlines()
    part1(lines)
    part2(lines)
