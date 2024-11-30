import string

def get_check_sum(crypt_name):
    counting = {}
    for l in crypt_name:
        counting[l] = crypt_name.count(l)
    sort_count = sorted(counting.items(),
                        key = lambda item: item[1],
                        reverse = True)
    key = ''.join([count[0] for count in sort_count])[:5]
    return key
    

def parse(line: str, part: int = 1):

    check_sum = line[-6:-1]
    sector_ID = line[:-7].split('-')[-1]
    crypt_name = line[:-7].split('-')[:-1]    
    if part == 1:
        crypt_name = ''.join(crypt_name)
    if part == 2:
        crypt_name = '-'.join(crypt_name)
        chain = string.ascii_lowercase
        new_name = ''
        for l in crypt_name:
            
            if l == '-':
                new_name += ' '
            else:
                code = chain.index(l)
                new_name += chain[(code + int(sector_ID)) % len(chain)]
        crypt_name = new_name
        print(crypt_name, sector_ID)
    crypt_name = ''.join(sorted(crypt_name))

    return check_sum == get_check_sum(crypt_name), int(sector_ID)

acc1 = 0
acc2 = 0

with open('input') as f:
    for line in f:
        real, ID = parse(line.rstrip('\n'))
        real2, ID2 = parse(line.rstrip('\n'), part = 2)

        if real:
            acc1 += ID
        if real2 :
            acc2 = ID2
        
print('part 1 :', acc1)
print('part 2 :', 'to get part 2 type python3 main.py | grep storage | grep object')
