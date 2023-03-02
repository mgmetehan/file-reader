import io
import struct

path = "/Users/mgmetehan/Desktop/chomar/deneme.docx"


data = open(path, "rb").read()

(eight, N) = struct.unpack("@II", data)