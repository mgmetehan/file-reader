import helper
# /Users/mgmetehan/Desktop/chomar/C-ProtStajyerproje.pdf
path = input("Enter your path: ")
result=helper.readFileByteByByte(path)
for i in range(2):
    print(result[i])