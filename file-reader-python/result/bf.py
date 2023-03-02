import io
from io import BytesIO

path = "/Users/mgmetehan/Desktop/chomar/deneme.xlsx"

buf = bytearray(2048)
with io.open(path, 'rb') as fp:
    size = fp.readinto(buf)
    print(buf[1])
    print(buf[0:size])
    int = int.from_bytes(buf[1:2], byteorder='big')
    print(int)
    b = BytesIO(buf)
    for byte in b: print(byte)


