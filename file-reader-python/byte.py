from io import BytesIO
path = "/Users/mgmetehan/Desktop/chomar/C-ProtStajyerproje.pdf"

with open(path, "rb") as fh:
    buf = BytesIO(fh.read())
    print(buf.read())
