

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
        pairs.sort()
        
        i = 0
        current = None
        while i < len(pairs):
            if not current:
                current = pairs[i]
            s, e = current 
            if i == len(pairs)-1:
                for seed in range(s,e):
                    yield seed
                break
            sn, en = pairs[i+1]

            if e>sn:
                current = s, en
            else:
                for seed in range(s,e):
                    yield seed
                current=None
            i += 1


    r = 0
    for i in gen_seeds():
        t = find_position(i)
        if not r or t < r:
            r = t
    print(r) 
    #lowest = min(map(find_position, gen_seeds()))
    #print(lowest)


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
