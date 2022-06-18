import struct


def uint16uint16uint8(x, start):
    size = struct.unpack("< H", x[start: start + 2])[0]
    add = struct.unpack("< H", x[start + 2: start + 4])[0]
    a = struct.unpack("< " + "B" * size, x[add: add + 1 * size])
    return list(a)


def D(x, start):
    return {
        'D1': struct.unpack("< q", x[start:start + 8])[0],
        'D2': struct.unpack("< I", x[start + 8:start + 12])[0],
        'D3': struct.unpack("< f", x[start + 12:start + 16])[0]
    }


def C(x, start):
    return {
        'C1': struct.unpack("< H", x[start:start + 2])[0],
        'C2': struct.unpack("< d", x[start + 2:start + 10])[0],
        'C3': list(struct.unpack('< 2b', x[start + 10:start + 12])),
        'C4': uint16uint16uint8(x, start + 12),
    }


def addressC(x, start):
    return struct.unpack("< I", x[start:start+4])[0]


def addressD(x, start):
    return struct.unpack("< I", x[start:start+4])[0]


def B(x, start):
    size = struct.unpack("< H", x[start: start + 2])[0]
    add = struct.unpack("< H", x[start + 2: start + 4])[0]

    return {
        'B1': [C(x, addressC(x, add+j*4)) for j in range(0, size)],
        'B2': D(x, addressD(x, start + 4)),
        'B3': list(struct.unpack('8h', x[start + 8:start + 24])),
        'B4': struct.unpack("< d", x[start + 24:start + 32])[0],
        'B5': struct.unpack("< i", x[start + 32:start + 36])[0],
        'B6': struct.unpack("< B", x[start + 36:start + 37])[0]
    }


def A(x, start):
    return {
        'A1': struct.unpack('< 4s', x[start:start+4])[0].decode('ascii'),
        'A2': struct.unpack('< d', x[start + 4:start + 12])[0],
        'A3': struct.unpack('< I', x[start + 12:start + 16])[0],
        'A4': struct.unpack("< q", x[start + 16:start + 24])[0],
        'A5': struct.unpack("< I", x[start + 24:start + 28])[0],
        'A6': struct.unpack("< Q", x[start + 28:start + 36])[0],
        'A7': B(x, start + 36),
        'A8': struct.unpack("< B", x[start + 73:start + 74])[0]
    }


def main(x):
    return A(x, 5)


print(main(b'BUTJ\xecrkvd&\x02\x04\xb6\x10j\xed\xbf\n\xfb\xb8l\x8c-e\xcf\x03\xc8\x07'
           b'\xbd\xddc\xbd\x9e\xcb"SM\xc6\xfbY\xff\x04\x00\x98\x00\xa8\x00\x00\x00H3s'
           b'\xbc\x98\x8d\x154\r\x81\xc1H\x9ew\x96\xff\xc0\xd9\x0cc\x7fs\xac?\x1a\xc81'
           b'\xb9O\x9eV=\xe9K\xac\xd3\xb1\xe1\xd2j\xe9\xbf1\x89\x02\x00O\x00\n\x12/'
           b'\xceta\x8b2\x1a=\xe3\xbfxl\x02\x00a\x002\x0brr\xc8\xb8sl\xd50I\xef?'
           b"@j\x03\x00s\x00i6\x1b\xd2P\xbd'[\x9c\xad\xd6\xbfu\xa1\x02\x00\x86\x00"
           b'Q\x00\x00\x00c\x00\x00\x00v\x00\x00\x00\x88\x00\x00\x00>\xec\x80\xe6'
           b'\x13q\xed\x04\x08tb\t\xa9\xd9\xbf\xbd'))

print(main(b'BUTJ\xecfbnq0=\xdb\xdbh=\xd5?\xf0\xb3\x81\x1c\x97t\xc5\x8dp\x1f\x93'
           b'b\xe2M\xb5\x01\xfe\x82!8Jr\xf2/\x03\x00\x86\x00\x92\x00\x00\x00V\xcd&'
           b'\xf1(\xb9\xc3\xb0\xd2)\x00\x83\xb7O4BPu\xc9S`\x90\xda\xbf}\x1c;R=\xe4\xce'
           b'\xb6\xf5\xca\xc6\xce\xe2\xe8\x01V\xed\xbf\xbc}\x02\x00O\x00\x89\xd1s'
           b'\xc9\x14\x90Qh\xa8C\xc9\xca\xbfe\xe1\x03\x00a\x00Q\xcc\xe0\xf8\xe4+\xed\x17'
           b'_7\xd7?\xfd\xf0\x02\x00t\x00Q\x00\x00\x00d\x00\x00\x00v\x00\x00\x00\x02\xb5'
           b'V\xa7\xa5R\xbd\x08\x05\xea\x9b\xa2\xc9\xac\x88\xbe'))
