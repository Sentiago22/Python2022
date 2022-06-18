import struct


def uint32uint16uint32(x, start):
    size = struct.unpack("> I", x[start: start + 4])[0]
    add = struct.unpack("> H", x[start + 4: start + 6])[0]
    a = struct.unpack("> " + "I" * size, x[add: add + 4 * size])
    return list(a)


def uint16uint32uint32(x, start):
    size = struct.unpack("> H", x[start: start + 2])[0]
    add = struct.unpack("> I", x[start + 2: start + 6])[0]
    a = struct.unpack("> " + "I" * size, x[add: add + 4 * size])
    return list(a)


def D(x, start):
    return {
        'D1': struct.unpack("> q", x[start + 64:start + 72])[0],
        'D2': struct.unpack("> I", x[start + 24:start + 28])[0],
        #'D3': struct.unpack("> d", x[start + 14:start + 22])[0]
    }


def C(x, start):
    return {
        'C1': struct.unpack("> H", x[start + 22:start + 24])[0],
        'C2': struct.unpack("> d", x[start + 14:start + 22])[0],
        #'C3': struct.unpack("> q", x[start + 64:start + 72])[0],
        #'C4': uint16uint32uint8(x, start + 58)
    }


def addressC(x, start):
    return struct.unpack("> I", x[start:start+4])[0]


def B(x, start):
    return {
        #'B1': C(x, addressC(x, start)),
        'B2': D(x, addressC(x, start)),
        #'B3': struct.unpack("> I", x[start + 5:start + 9])[0],
        'B4': struct.unpack("> d", x[start + 9:start + 17])[0],
        '''
        'B5': [struct.unpack("> H", x[start + 17:start + 19])[0],
               struct.unpack("> H", x[start + 19:start + 21])[0],
               struct.unpack("> H", x[start + 21:start + 23])[0],
               struct.unpack("> H", x[start + 23:start + 25])[0]],
        '''
        'B6': struct.unpack("> d", x[start + 25:start + 33])[0]
    }


def A(x, start):
    return {
        'A1': B(x, start),
        'A2': struct.unpack("> H", x[start + 33:start + 35])[0],
        'A3': struct.unpack("> I", x[start + 35:start + 39])[0],
        'A4': struct.unpack("> H", x[start + 39:start + 41])[0],
    }


def main(x):
    return A(x, 5)

print(main(b"\xcbNMEY\x00\x00\x00^c\x99\x82.\xa6?\xcc'\xe6\xb0\x11\xc2\xe0\xb0ww\xbc<\\"
 b'\xbd\xd4?\xe8\xfc\xd4B\x8d\xf2\xe0\xf3\xd1H\xc7\xbe\x00(#{\xfe'
 b'\xeb\x87\xf9\x0c.\xbeG,}\xd9\xbb\xf3\xfa\xf3\xe7\x92\ra\xaeKqW\xa0S'
 b'5\xce\x0fo\xc6{W\x81jN\xe2P\x02\x06\x9d`K\r\xd0\xf7d\x15\xc0fL\xfd\x89\x84'
 b'\\A\x00\x00\x00\x05\x00.?\xd4\x10\xd1\x843+X\x90\xd4-is\x19\x85kN6\xc1\xd2'
 b'&\xdeA\x00\x00\x00\x04\x00B?\xc8\xbfT\xb1c\x10`\x89~\x10\x98\xbd*#'
 b'\x00\x03\x00\x00\x00RtK\x12c"o\x14\xb8'))