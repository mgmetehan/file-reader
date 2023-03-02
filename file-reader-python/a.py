path = "/Users/mgmetehan/Desktop/chomar/deneme.xlsx"

with open(path, "rb") as fData:
    lines = fData.read().splitlines()
    lines = [line.decode("cp856", errors="ignore") for line in lines]
    print(lines)