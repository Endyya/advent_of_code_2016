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
