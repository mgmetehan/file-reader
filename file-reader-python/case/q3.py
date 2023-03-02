import helper
# /Users/mgmetehan/Desktop/chomar/
path = input("Enter your path: ")
search_string = input("Enter your search string: ")
list=helper.listFilesInDir(path)

listLength=len(list)

for i in range(listLength):
    newFile = str(list[i])
    newPath = str(path + newFile)
    helper.searchForStringInFile(newPath, search_string.encode())
