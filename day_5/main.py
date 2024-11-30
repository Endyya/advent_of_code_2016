import hashlib as hl

code = 'abbhdwsy'

password = ''
counter = 0
while len(password) < 8:
    to_hash = code + str(counter)
    hashing = hl.md5(to_hash.encode()).hexdigest()
    counter += 1
    if hashing[:5] == '00000':
        password += hashing[5]
        

print('part 1 :', password)

password = 8 * ['0']
possible_pos = ['0', '1', '2', '3', '4', '5', '6', '7']
counter = 0

while len(possible_pos) > 0:
    to_hash = code + str(counter)
    hashing = hl.md5(to_hash.encode()).hexdigest()
    counter += 1

    if hashing[:5] == '00000':
        pos = hashing[5]
        if pos in possible_pos:
            password[int(pos)] = hashing[6]
            possible_pos.remove(pos)

print('part 2 :', ''.join(password))
            
