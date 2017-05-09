import operator

def get_base64_dict():
    ascii_dict = dict(sorted(get_printable_asciidict().items(), key=operator.itemgetter(0)))
    base64_dict = dict()
    b64_index_numbers = 52
    b64_index_lower = 26
    b64_index_upper = 0

    for key, value in ascii_dict.iteritems():
        if int(key) == 43: 
            base64_dict[value] = 62

        if int(key) == 47:
            base64_dict[value] = 63

        if int(key) in range(48,57):
            base64_dict[value] = b64_index_numbers
            b64_index_numbers += 1
        
        if int(key) in range(65,90):
            base64_dict[value] = b64_index_upper
            b64_index_upper += 1

        if int(key) in range(97,122):
            base64_dict[value] = b64_index_lower
            b64_index_lower += 1
            
    return base64_dict

def get_printable_asciidict():
    ascii_dict = dict()

    for i in range (32,122):
        ascii_dict[i] = chr(i)

    return ascii_dict

encrypted = 'QW== QT== QT== QQ== QU== Qd== QU== Qd== QX== QV== QW== Qe== QT== QR== QU== QT== QT== QU== QX== QU== QT== QR== QT== QQ== QW== Qe=='
print "String with encrypted message: ", encrypted

enc_array = encrypted.split(' ') 
base64dict = dict(sorted(get_base64_dict().items(), key=operator.itemgetter(1)))

#     A
# 010000|01||0110||000000|000000 
#    16    22     0     0     
#    Q     W      =     =

# 010000|01||0011||000000|000000
#   16     19     0     0
#   Q       T     =     =

chars_with_ignored_bytes = ''
result = []

for i in range(0, len(enc_array)):
    chars_with_ignored_bytes += enc_array[i][1]

for i in xrange(0, len(chars_with_ignored_bytes), 2):
    if chars_with_ignored_bytes[i] in base64dict:
        result.append(format(int(base64dict[chars_with_ignored_bytes[i]]) & 0xf, '#06b') + format(int(base64dict[chars_with_ignored_bytes[i + 1]]) & 0xf, '#06b')[2:])

print("The message is: " + ''.join([chr(int(result[i], 2)) for i in range(0, len(result))]))


