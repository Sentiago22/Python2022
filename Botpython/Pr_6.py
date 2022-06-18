def main(x):
    A = x & 0b111111111111
    B = (x >> 12) & 0b111
    C = (x >> 15) & 0b11111111111
    D = (x >> 26) & 0b1
    E = (x >> 27) & 0b111
    F = (x >> 30) & 0b11
    result = 0
    result |= B
    result |= D << 3
    result |= F << 4
    result |= C << 6
    result |= E << 17
    result |= A << 20
    return result

print(hex(main(0x43ec82bf)))
print(hex(main(0xf74b2dbd)))


