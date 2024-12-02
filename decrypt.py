def decrypt(word):
    offset = 4
    result = ''
    for x in range(offset):
        counter = -1 - x
    
        for c in word:   
            counter += 1
            if counter % offset == 0:
                result += c
    return result

print(decrypt('Pmacr thaIieknortfnhiosekrsiumit'))
