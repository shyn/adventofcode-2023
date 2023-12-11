import os

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input'), 'r') as f:
    lines = f.readlines()


constrains = (12, 13, 14)

def easy():
    ret = 0
    for line in lines:
        line = line.strip()
        if not line:
            continue
        gn, ss = line.split(':')
        gn = int(gn[5:])
        flag = False
        for show in ss.split(';'):
            stop = False
            for g in show.split(','):
                num, color = g.split()
                if color == 'red' and int(num) > constrains[0]:
                    stop = True
                    break
                if color == 'green' and int(num) > constrains[1]:
                    stop = True
                    break
                if color == 'blue' and int(num) > constrains[2]:
                    stop = True
                    break
            if stop:
                flag = True
                break
        if flag:
            continue
        ret += gn
    print(ret)


def hard():
    ret = 0
    for line in lines:
        line = line.strip()
        if not line:
            continue
        gn, ss = line.split(':')
        gn = int(gn[5:])
        mr, mg, mb = 1, 1, 1
        for show in ss.split(';'):
            for g in show.split(','):
                num, color = g.split()
                if color == 'red' and int(num) > mr:
                    mr = int(num)
                    continue
                if color == 'green' and int(num) > mg:
                    mg = int(num)
                    continue
                if color == 'blue' and int(num) > mb:
                    mb = int(num)
                    continue
        ret += mr * mg * mb
    print(ret)


if __name__ == '__main__':
    import sys
    args = sys.argv[1:]
    if len(args) == 0:
        print('default run easy')
        easy()
    else:
        eval(f'{sys.argv[1]}()')


