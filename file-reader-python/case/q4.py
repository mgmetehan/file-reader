import helper
# /Users/mgmetehan/Desktop/chomar/
path = input("Enter your path: ")
search_string = input("Enter your search string: ")
list=helper.listFilesInDir(path)

listLength=len(list)

for i in range(listLength):
    newFile = str(list[i])
    newPath = str(path + newFile)
    twoBytes=helper.readFileAllByte(newPath)
    if twoBytes[0:2]==b"MZ":
        helper.searchForStringInFile(newPath, search_string.encode())
    else:
        print("This file is not a PE file")