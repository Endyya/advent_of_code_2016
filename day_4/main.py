def get_check_sum(crypt_name):
    counting = {}
    for l in crypt_name:
        counting[l] = crypt_name.count(l)
    sort_count = sorted(counting.items(),
                        key = lambda item: item[1],
                        reverse = True)
    key = ''.join([count[0] for count in sort_count])[:5]
    return key
    

def parse(line: str):

    check_sum = line[-6:-1]
    sector_ID = line[:-7].split('-')[-1]
    crypt_name = line[:-7].split('-')[:-1]
    crypt_name = ''.join(crypt_name)
    crypt_name = ''.join(sorted(crypt_name))

    return check_sum == get_check_sum(crypt_name), int(sector_ID)

acc1 = 0

with open('input') as f:
    for line in f:
        real, ID = parse(line.rstrip('\n'))
        if real:
            acc1 += ID
        
print('part 1 :', acc1)
