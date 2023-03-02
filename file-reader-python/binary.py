# read textfile into string
path = "/Users/mgmetehan/Desktop/chomar/deneme.xlsx"

with open(path, 'r') as txtfile:
    mytextstring = txtfile.read()

# change text into a binary array
binarray = ' '.join(format(ch, 'b') for ch in bytearray(mytextstring))

# save the file
with open('binfileName', 'br+') as binfile:
    binfile.write(binarray)