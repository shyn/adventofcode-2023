import string
with open('input', 'r') as f:
    data = []
    for line in f:
        line = line.strip()
        data.append(line)

def easy():
    def parse(line):
        ds = []
        for c in line:
            if c.isdigit():
                ds.append(c)
        return int(f'{ds[0]}{ds[-1]}')

    print(sum(map(parse, data)))

def hard():
    word_digit = (
            'one',
            'two',
            'three',
            'four',
            'five',
            'six',
            'seven',
            'eight',
            'nine',
            )
    prefix_tree = {}
    # build prefix tree
    for v, word in enumerate(word_digit):
        cur = prefix_tree
        for c in word[:-1]:
            cur = cur.setdefault(c, {})
        cur[word[-1]] = v

    def parse(line):
        ds = []
        for i, c in enumerate(line):
            if c.isdigit():
                ds.append(c)
            else:
                for j, w in enumerate(word_digit):
                    if line[i:].startswith(w):
                        ds.append(j+1)
                        break    
        return int(f'{ds[0]}{ds[-1]}')

    print(sum(map(parse, data)))

